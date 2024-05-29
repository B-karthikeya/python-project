import socket

s = socket.socket()
print("socket created")
s.bind(('127.0.0.1', 8080))
s.listen(3)
print("socket bind")
while True:
     c, addr = s.accept()
     print("client connected",addr)
     c.send("welcome")
     c.close()