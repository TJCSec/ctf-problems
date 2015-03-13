#!/usr/bin/python2
from pwn import *
context(arch='i386', os='linux')

def send(d):
    r.send(d.encode('rot13'))

r = remote('127.0.0.1',8086)
print r.recvlines(2)
for i in range(256):
    send('a\n')
r.send('\n')
res = r.recvall()
print res
print len(res)
r.close()
