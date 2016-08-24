# Author: Terry Liu
# License: MIT

import os
import base64
from pyws import PWSocket
from pyws import pwhandshake

_WS_DEFAULT_PORT = 80
_WSS_DEFAULT_PORT = 443

class PWClient:
    'The websocket client'
    def __init__(self):
        self.__sock = PWSocket()
        self.__userAddHandshake = None

    def start_connection(self, url, port):
        'connect to server and send HTTP handshake'

        if url[0] is not 'w':
            print 'Wrong websocket url format. Example: ws://www.example.com'
            return False
        if isinstance(port, int) is not True:
            print 'Wrong type for port'
            return False

        # TODO: try urlparse()
        [secureConn, host] = url.split('://')
        if (secureConn == 'wss'):
            print 'Use TLS connection'
        self.__sock.connect(host, port)

        if port != _WS_DEFAULT_PORT and port != _WSS_DEFAULT_PORT:
            host = ('%s:%d' % (host, port))

        pwhandshake.start_handshaking(self.__sock, host, self.__userAddHandshake)

    def set_header(self, key, value):
        if self.__userAddHandshake is None:
            self.__userAddHandshake = {}
        self.__userAddHandshake[key] = value
