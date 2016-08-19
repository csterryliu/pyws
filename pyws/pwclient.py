# Author: Terry Liu
# License: MIT

import os
import base64
from pyws import PWSocket

_WS_IMPLEMENTED_VERSION = '13'
_WSKEY_RANDOM_BYTES_SIZE = 16

class PWClient:
    'The websocket client'
    def __init__(self):
        self.__sock = PWSocket()
        self.__wsVersion = _WS_IMPLEMENTED_VERSION
        self.__handhakeDic = {'Connection': 'Upgrade', 'Upgrade': 'websocket', 'Sec-WebSocket-Version': self.__wsVersion}

    def start_connection(self, url, port):
        'connect to server and send HTTP handshake'

        if url[0] is not 'w':
            print 'Wrong websocket url format. Example: ws://www.example.com'
            return False
        # TODO: check the type of port

        # TODO: try urlparse()
        [secureConn, host] = url.split('://')
        if (secureConn == 'wss'):
            print 'Use TLS connection'
        self.__sock.connect(host, port)

        self.set_header('Host', host)
        self.set_header('Sec-WebSocket-Key', self.__produce_websocket_key())
        handshake_msg = self.__create_handshake()
        self.__sock.send(handshake_msg)

        #recv_bytes = self.__sock.recv()
        #print recv_bytes

    def set_header(self, key, value):
        self.__handhakeDic[key] = value

    def __create_handshake(self):
        #TODO: change request-URI
        handshake_msg = 'GET / HTTP/1.1\n'
        for key, value in self.__handhakeDic.iteritems() :
            handshake_msg += key + ': ' + value + '\r\n'
        handshake_msg += '\r\n'
        print 'handshake_msg: ' + handshake_msg
        return handshake_msg

    def __produce_websocket_key(self):
        ran_bytes = os.urandom(_WSKEY_RANDOM_BYTES_SIZE)
        key_str = ran_bytes.encode('base64')
        return str.rstrip(key_str, '\n')
