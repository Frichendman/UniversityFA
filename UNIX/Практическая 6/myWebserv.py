#!/usr/bin/env python
import os 
homedir=r"C:\Users\Frich\Desktop\Pr6"
def load_file(path):  
         
    with open(path) as f:
        return f.read(), 200
 
import socket
sock = socket.socket()
try:
  sock.bind(('', 80))
except OSError:
  sock.bind(('', 8080))
sock.listen(5)
conn, addr = sock.accept()
print("Connected", addr)
data = conn.recv(8192)
msg = data.decode()
print(msg)
#path = homedir + "\index.html"
path = "index.html"
body, status_code = load_file(path)
#header = get_header(status_code, path)
conn.send((body).encode())
conn.close()


