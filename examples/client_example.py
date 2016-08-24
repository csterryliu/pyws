#!/usr/bin/python

from pyws import PWClient

print """
----------------------------------------------------------
pyws - Websocket client/server implementation for Python

This is the usage example for a websocket client.

Author: Terry Liu
License: MIT
----------------------------------------------------------
"""

c = PWClient()
c.set_header('test', '123')
c.start_connection('ws://127.0.0.1', 3000)
