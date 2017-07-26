#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import thread
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostname()  # Get local machine name
port = 40000                 # Reserve a port for your service.


def forward_send(c, l):
    while True:
        msg = c.recv(1024)
        print msg
        for i in l:
            if i != c:
              i.sendall(msg)

print 'Server started!'
print 'Waiting for clients...'

s.bind(('192.168.1.31', port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.
l = []
print 'aaa'
while True:
    c, addr = s.accept()     # Establish connection with client. 
    print 'get connected {}'.format(addr)
    l.append(c)
    thread.start_new_thread(forward_send, (c, l))