import socket
c =socket.socket()
c.connect(('127.0.0.1', 8080))
print(c.recv(1024))