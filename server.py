import socket
from protocol import Protocol, g, n

PORT = 8888

x = 131 # only Alice knows this

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
prot = Protocol(s)
prot.open(PORT)

bobSends, addr, _ = prot.read()
publicKey = (int(bobSends) ** x) % n

aliceSends = (g ** x) % n
prot.write(str(aliceSends), addr)

while 1:
  data, addr, error = prot.sread(publicKey)

  if error == 1:
    print('Error code 1. Data does not corresponds to checksum')
  else:
    if not data:
      break

    reply = data

    prot.swrite(reply, addr, publicKey)

    print(addr[0], str(addr[1]), data)

prot.close()
