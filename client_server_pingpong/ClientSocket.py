import socket

s = socket.socket()

s.connect(('127.0.0.1', 2632 ))
s.send(bytes("28".encode('utf-8')))
m = s.recv(2048)


print(str(m))