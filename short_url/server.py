from flask import Flask
from flask import abort, request, redirect, render_template, url_for
import re
import redis


app = Flask(__name__)
r = redis.Redis()


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


def shorten_url(url):
    a1 = "0123456789"
    a2 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    seed = int(base_conv(r.get("last_url"), a2, a1))

    a = 9533525225  # redact
    c = 42933  # redact
    m = 573824839043  # redact

    v1 = str((a * seed + c) % m)
    v2 = base_conv(v1, a1, a2)

    r.set(v2, url)
    r.set("last_url", v2)
    r.incr("num_shortened")

    return v2


@app.route("/", methods=["GET", "POST"])
def index():
    hits = r.incr("hit_count")
    context = {
        "hits": hits,
        "shortened": len(r.keys()) - 3,
    }

    if request.method == "GET":
        return render_template("index.html", **context)
    else:
        if url_valid(request.form.get("url", "")):
            url = request.form["url"]
            url_hash = shorten_url(url)
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
    if not re.match("^[a-zA-Z0-9]+$", url_hash):
        abort(404)
    url = r.get(url_hash)
    if url:
        return redirect(url)
    else:
        abort(404)


if __name__ == "__main__":
    secret_url = "http://pastebin.com/SMtP9z7B"  # redact

    r.flushall()
    r.set("hit_count", 0)
    r.set("num_shortened", 0)
    r.set("last_url", "fabcab")
    shorten_url(secret_url)

    app.debug = True
    app.run()
