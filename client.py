import socket	#for sockets
from protocol import Protocol

# create dgram udp socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
prot = Protocol(s)

host = 'localhost'
port = 8888;

while 1:
	msg = input('Enter message to send : ')

	prot.write(msg.encode(), (host, port))

	reply, addr = prot.read()

	print(b'Server reply : ' + reply)
