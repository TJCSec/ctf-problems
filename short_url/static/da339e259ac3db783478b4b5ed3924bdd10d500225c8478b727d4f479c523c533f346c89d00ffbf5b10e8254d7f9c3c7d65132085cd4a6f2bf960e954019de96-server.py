from flask import Flask
from flask import abort, request, redirect, render_template, url_for, session
from Crypto.Cipher import AES
from pickle import loads, dumps
import re


app = Flask(__name__)
app.secret_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'

secret_url = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"  # redact

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[:-ord(s[len(s)-1:])]


def enc(lasturl):
    obj = AES.new(app.secret_key)
    return obj.encrypt(pad(lasturl))

def dec(lasturl):
    obj = AES.new(app.secret_key)
    return unpad(obj.decrypt(lasturl))

def url_valid(url):
    # Ripped from Django
    regex = re.compile(
            r"^(?:[a-z0-9\.\-]*)://"  # scheme is validated separately
            r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}(?<!-)\.?)|"  # domain...
            r"localhost|"  # localhost...
            r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|"  # ...or ipv4
            r"\[?[A-F0-9]*:[A-F0-9:]+\]?)"  # ...or ipv6
            r"(?::\d+)?"  # optional port
            r"(?:/?|[/?]\S+)$", re.IGNORECASE)
    schemes = ["http", "https"]
    scheme = url.split("://")[0].lower()
    return (scheme in schemes) and bool(regex.search(url))


def base_conv(v1, a1, a2):
    n1 = {c: i for i, c in enumerate(a1)}
    b1 = len(a1)
    b2 = len(a2)

    d1 = 0
    for i, c in enumerate(v1):
        d1 += n1[c] * pow(b1, len(v1) - i - 1)

    v2 = ""
    while d1:
        v2 = a2[d1 % b2] + v2
        d1 //= b2

    return v2


def shorten_url(s, url):
    a1 = "0123456789"
    a2 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    seed = int(base_conv(dec(s.get("last_url",enc("fabcab"))), a2, a1))

    a = xxxxxxxx  # redact
    c = xxxxxx  # redact
    m = xxxxxxxxx  # redact

    v1 = str((a * seed + c) % m)
    v2 = base_conv(v1, a1, a2)

    existurls = loads(dec(s["urls"]))
    existurls[v2] = url
    s["urls"] = enc(dumps(existurls))
    s["last_url"] = enc(v2)
    s["num_shortened"] += 1

    return v2


@app.route("/", methods=["GET", "POST"])
def index():
    check_session(session)

    session["hit_count"] += 1
    hits = session["hit_count"]

    context = {
        "hits": hits,
        "shortened": len(loads(dec(session["urls"]))),
    }

    if request.method == "GET":
        return render_template("index.html", **context)
    else:
        if url_valid(request.form.get("url", "")):
            url = request.form["url"]
            url_hash = shorten_url(session, url)
            context["shortened"] += 1
            abs_url = url_for("follow_shortened_url",
                              url_hash=url_hash,
                              _external=True)
            context["shortened_url"] = abs_url
        else:
            context["error"] = True
            context["target_url"] = request.form.get("url", "")
        return render_template("index.html", **context)


@app.route("/<url_hash>", methods=["GET"])
def follow_shortened_url(url_hash):
    check_session(session)

    if not re.match("^[a-zA-Z0-9]+$", url_hash):
        abort(404)
    url = loads(dec(session["urls"])).get(url_hash)
    if url:
        return redirect(url)
    else:
        abort(404)

def check_session(s):
    if "updated2" not in s:
        s.clear()
        
    if "hit_count" not in s:
        s["hit_count"] = 0
        s["num_shortened"] = 0
        s["last_url"] = enc("fabcab")
        s["urls"] = enc(dumps({}))
        s["updated2"] = True
        shorten_url(s, secret_url)
    
if __name__ == "__main__":

    app.debug = True
    app.run()
