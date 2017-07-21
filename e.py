#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import thread
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 50000                # Reserve a port for your service.

def thread_output(msg,l):
    for i in l:
        i.sendall(msg)

print 'Server started!'
print 'Waiting for clients...'

s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.
l = []
while True:
    c, addr = s.accept()     # Establish connection with client.
    l.append(c)
    msg = raw_input('SERVER >> ')
    thread.start_new_thread(thread_output, (msg,l))



