#!/usr/bin/env python
 
import socket
import threading
 
class T(threading.Thread):
  def __init__(self, n):
    threading.Thread.__init__(self, name="t" + n)
    self.n = n
  def run(self):
    print ("Процесс", self.n)

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', 8291))
sock.listen(1)
conn, addr = sock.accept()
p1 = T("1")
p2 = T("2")
p1.start()
p2.start()
 
print('connected:', addr)

while True: 
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        conn.send(data.upper().encode())
        if "exit".lower() in data:
            break
    if ("exit".lower() in data) or not data:
        break
conn.close()
