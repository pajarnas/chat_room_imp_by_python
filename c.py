import socket
s = socket.socket()
s.connect(("192.168.1.31",50000))
while True:
    print s.recv(1024)
