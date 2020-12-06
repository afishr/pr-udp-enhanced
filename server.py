import socket
from protocol import Protocol

PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
prot = Protocol(s)
prot.open(PORT)

while 1:
	data, addr = prot.read()

	if not data:
		break

	reply = data

	prot.write(reply, addr)

	print(addr[0], str(addr[1]), data.strip())

prot.close()
