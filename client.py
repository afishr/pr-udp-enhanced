import socket	#for sockets
from protocol import Protocol, g, n

y = 533 # only Bob knows this

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
prot = Protocol(s)

host = 'localhost'
port = 8888;

bobSends = (g**y)%n
prot.write(str(bobSends), (host, port))

aliceSends, addr, _ = prot.read()
publicKey = (int(aliceSends) ** y) % n

while 1:
  msg = input()

  prot.swrite(msg, (host, port), publicKey)

  reply, addr, error = prot.sread(publicKey)

  if (error == 1):
    print('Error code 1. Data does not corresponds to checksum')
  else:
    print(reply)
