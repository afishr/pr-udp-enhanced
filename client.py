import socket	#for sockets
from protocol import Protocol

# create dgram udp socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
prot = Protocol(s)

host = 'localhost'
port = 8888;

while 1:
  msg = input('Enter message to send : ')

  prot.write(msg, (host, port))

  reply, addr, error = prot.read()

  if (error == 1):
    print('Error code 1. Data does not corresponds to checksum')
  else:
    print(reply)
