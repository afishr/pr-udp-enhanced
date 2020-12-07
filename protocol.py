import json
import hashlib
import base64

BUFFER_SIZE = 1024

n = 22 # publicly known
g = 42 # publicly known

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

    data = json.loads(data.decode())['data']

    return data, addr, error

  def write(self, value, address):
    self.socket.sendto(self.__sign(value), address)

  def sread(self, key):
    error = 0

    d = self.socket.recvfrom(BUFFER_SIZE)
    data = d[0]
    addr = d[1]

    data = self.__decrypt(key, data)

    if not self.__verify(data):
      error = 1

    data = json.loads(data)['data']

    return data, addr, error

  def swrite(self, value, address, key):
    self.socket.sendto(self.__encrypt(key, self.__sign(value).decode()), address)

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

  def __encrypt(self, key, string):
    encoded_chars = []
    for i in range(len(string)):
      encoded_c = chr(ord(string[i]) + key % 256)
      encoded_chars.append(encoded_c)
    encoded_string = "".join(encoded_chars)
    return base64.urlsafe_b64encode(encoded_string.encode())

  def __decrypt(self, key, string):
    decoded_chars = []
    string = base64.urlsafe_b64decode(string).decode()
    for i in range(len(string)):
      encoded_c = chr(ord(string[i]) - key % 256)
      decoded_chars.append(encoded_c)
    encoded_string = "".join(decoded_chars)
    return ''.join(decoded_chars)

