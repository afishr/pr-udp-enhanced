import socket
from protocol import Protocol

PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
prot = Protocol(s)
prot.open(PORT)

while 1:
  data, addr, error = prot.read()

  if error == 1:
    print('Error code 1. Data does not corresponds to checksum')
  else:
    if not data:
      break

    reply = data

    prot.write(reply.decode(), addr)

    print(addr[0], str(addr[1]), data)

prot.close()
