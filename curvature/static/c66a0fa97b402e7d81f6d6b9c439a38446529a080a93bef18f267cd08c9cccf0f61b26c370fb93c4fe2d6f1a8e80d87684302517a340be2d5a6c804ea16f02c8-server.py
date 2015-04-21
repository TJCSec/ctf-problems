#!/usr/bin/env python

import SocketServer, threading

PORT = 8089
FLAG = int("REDACTED".encode("hex"),16) # Find me!

A = 0x7D5A0975FC2C3057EEF67530417AFFE7FB8055C126DC5C6CE94A4B44F330B5D9
B = 0x26DC5C6CE94A4B44F330B5D9BBD77CBF958416295CF7E1CE6BCCDC18FF8C07B6
P = 0xA9FB57DBA1EEA9BC3E660A909D838D726E3BF623D52620282013481D1F6E5377
# Curve is y^2 = x^3 + Ax + B, all modulo P

# From Wikibooks, because I'm lazy
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def inv(a):
    gcd, x, y = egcd(a % P, P)
    if gcd != 1:
        raise Exception('No modular inverse')
    else:
        return x % P

def add(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    l = ((b[1] - a[1]) * inv(b[0] - a[0])) % P
    x = (l*l - a[0] - b[0]) % P
    y = (l*(a[0] - x) - a[1]) % P
    return (x,y)

def double(a):
    if a == 0:
        return a
    l = ((3*a[0]*a[0] + A) * inv(2*a[1])) % P
    x = (l*l - 2*a[0]) % P
    y = (l*(a[0] - x) - a[1]) % P
    return (x,y)

def multiply(point, exponent):
    # No timing attack for you :P
    r0 = 0
    r1 = point
    for i in bin(exponent)[2:]:
        if i == '0':
            r1 = add(r0, r1)
            r0 = double(r0)
        else:
            r0 = add(r0, r1)
            r1 = double(r1)
    return r0

class ThreadedServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    allow_reuse_address = True

class Handler(SocketServer.BaseRequestHandler):
    def handle(self):
        self.request.send("Send me points to exponentiate!\n")
        self.request.send("Format: \"x y\"\n")

        while True:
            point = self.request.recv(4096)
            x, y = [int(i) for i in point.strip().split()]
            x2, y2 = multiply((x, y), FLAG)
            self.request.send("Your point:\n")
            self.request.send("(%d, %d)\n" % (x2, y2))

server = ThreadedServer(('0.0.0.0', PORT), Handler)
server_thread = threading.Thread(target=server.serve_forever)
server_thread.daemon = True
server_thread.start()
server_thread.join()
