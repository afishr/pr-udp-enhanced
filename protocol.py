BUFFER_SIZE = 1024

class Protocol:
  def __init__(self, socket):
    self.socket = socket

  def open(self, server_port):
    self.socket.bind(('localhost', server_port))

  def close(self):
    self.socket.close()

  def read(self):
    d = self.socket.recvfrom(BUFFER_SIZE)
    data = d[0]
    addr = d[1]

    return data, addr

  def write(self, value, address):
    self.socket.sendto(value, address)
