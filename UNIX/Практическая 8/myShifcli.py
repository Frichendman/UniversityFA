#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import pickle

sock = socket.socket()
sock.connect(('localhost', 8291))

while True:
    p, g, a = 7, 5, 3
    A = g ** a % p
    sock.send(pickle.dumps((p, g, A)))
    msg = sock.recv(1024)
    B = pickle.loads(msg)
    K = B ** a % p
    print("K =", K)
    break

