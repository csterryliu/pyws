# Author: Terry Liu
# License: MIT

import os

_WS_KEY_RANDOM_SIZE = 16
_WS_IMPLEMENTED_VERSION = 13

def start_handshaking(sock, host, user_add_handshake=None):
    handshake_msg = _create_handshake(host, user_add_handshake)
    sock.send(handshake_msg)
    #recv_bytes = self.__sock.recv()
    #print recv_bytes

def _create_handshake(host, user_add_handshake):
    handshake = {'Connection': 'Upgrade', 'Upgrade': 'websocket', 'Sec-WebSocket-Version': ("%d" % _WS_IMPLEMENTED_VERSION)}
    handshake['Host'] = host
    handshake['Sec-WebSocket-Key'] = _produce_websocket_key()

    #TODO: change request-URI
    handshake_msg = 'GET / HTTP/1.1\n'
    for key, value in handshake.iteritems() :
        handshake_msg += key + ': ' + value + '\r\n'
    if user_add_handshake is not None:
        for key, value in user_add_handshake.iteritems():
            handshake_msg += key + ': ' + value + '\r\n'
    handshake_msg += '\r\n'
    print 'handshake_msg: ' + handshake_msg
    return handshake_msg

def _produce_websocket_key():
    ran_bytes = os.urandom(_WS_KEY_RANDOM_SIZE)
    key_str = ran_bytes.encode('base64')
    return str.rstrip(key_str, '\n')
