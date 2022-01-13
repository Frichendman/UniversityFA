#!/usr/bin/env python
 
import socket
import pickle
 
sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', 8291))
sock.listen(1)
conn, addr = sock.accept()
 
print('connected:', addr)

while True: 
    while True:
        msg = conn.recv(1024)
        b = 9
        p, g, A = pickle.loads(msg)
        B = g ** b % p
        conn.send(pickle.dumps(B))
        K = A ** b % p
        print("K =", K)
        break

conn.close()
