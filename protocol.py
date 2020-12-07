import json
import hashlib

BUFFER_SIZE = 1024

class Protocol:
  def __init__(self, socket):
    self.socket = socket

  def open(self, server_port):
    self.socket.bind(('localhost', server_port))

  def close(self):
    self.socket.close()

  def read(self):
    error = 0

    d = self.socket.recvfrom(BUFFER_SIZE)
    data = d[0]
    addr = d[1]

    if not self.__verify(data):
      error = 1

    return data, addr, error

  def write(self, value, address):
    self.socket.sendto(self.__sign(value), address)

  def __sign(self, payload):
    data = json.dumps({
      "data": payload,
      "checksum": hashlib.md5(payload.encode()).hexdigest()
    }).encode()

    return data

  def __verify(self, payload):
    data = json.loads(payload)

    checksum = data['checksum']
    computedChecksum = hashlib.md5(data['data'].encode()).hexdigest()

    return checksum == computedChecksum
