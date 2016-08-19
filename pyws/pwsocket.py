# Author: Terry Liu
# License: MIT

import socket

class PWSocket:
    'The class which wraps the socket module and provides basic socket operations'
    def __init__(self):
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __del__(self):
        print 'closing socket...'
        self.__sock.close()

    def connect(self, addr, port):
        print 'connecting to ' + addr + ':' + str(port)
        self.__sock.connect((addr, port))

    def send(self, data):
        self.__sock.send(data)

    def recv(self, bufsize=1024):
        return self.__sock.recv(bufsize)

    def close(self):
        self.__sock.close()
