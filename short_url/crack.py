import requests
from bs4 import BeautifulSoup
from fractions import gcd
import uuid

a10 = "0123456789"
a62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

s = requests.session()


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


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("modular inverse does not exist")
    else:
        return x % m


k = 20
X = []
id_o = 0

for i in range(k):
    data = {
        "url": "http://www.google.com/%s" % uuid.uuid4()
    }

    r = s.post("http://127.0.0.1:8095", data=data)
    html = BeautifulSoup(r.text)
    url_id = int(html.find_all("li")[1].text.split()[2]) - 1
    if i == 0:
        id_o = url_id
    else:
        assert url_id == i + id_o

    url_hash = html.find("a").text.split("/")[3]
    d = int(base_conv(url_hash, a62, a10))
    X.append(d)

t = []
for i in range(k-1):
    t.append(X[i+1] - X[i])

u = []
for i in range(k-3):
    u.append(abs(t[i+2] * t[i] - t[i+1]**2))

m = reduce(gcd, u)
a = (modinv((X[0] - X[1]) % m, m) * (X[1] - X[2])) % m
c = (X[1] - a * X[0]) % m


hash_int = (a * int(base_conv("fabcab", a62, a10)) + c) % m
secret_hash = base_conv(str(hash_int), a10, a62)
print("Secret Hash: " + secret_hash)
