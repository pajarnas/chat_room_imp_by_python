import socket
import thread
s = socket.socket()
s.connect(("192.168.1.31",50000))

def recv_message():
  while True:
    print s.recv(1024)

thread.start_new_thread(recv_message,())
while True:
  msg = str(socket.gethostname())+':' + raw_input("{}".format('someone>>:'))
  s.sendall(msg) 
