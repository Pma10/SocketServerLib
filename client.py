import comm

import network.common as comn
from socket import *
from threading import Thread


class Client:
    def __init__(self, host='127.0.0.1', port=9999):
        self.socket = socket()
        self.socket.connect((host, port))

    def __del__(self):
        self.socket.close()

    def send(self, data):
        self.socket.send(data)

    def recv(self):
        return self.socket.recv(comn.BUF_SIZE)
