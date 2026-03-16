import collections
from json import loads,dumps
import os
import socket

PORT = os.environ.get('AP_PORT')
HOST = os.environ.get('AP_HOST')
HANDSHAKE = os.environ.get('AP_HANDSHAKE')
Result = collections.namedtuple('Result', 'id,result,error')

class Android(object):

  def __init__(self, addr=None):
    if addr is None:
      addr = HOST, PORT
    client = socket.create_connection(addr).makefile("rw")
    self._write = client.write
    self._flush = client.flush
    self._readline = client.readline
    self._id = 0
    self._authenticate(HANDSHAKE)

  def _rpc(self, method, *args):
    self._write(dumps({
                'id': self._id,
                'method': method,
                'params': args 
                }) + '\n')
    self._flush()
    self._id += 1
    result = loads(self._readline())
    if result['error'] is not None:
      print(result['error'])
    # namedtuple doesn't work with unicode keys.
    return Result(result['id'],
                  result['result'],
                  result['error'] )

  def __getattr__(self, name):
    return lambda *args:self._rpc(name, *args)
