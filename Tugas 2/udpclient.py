import socket
import os

TARGET_IP = "127.0.0.1"
TARGET_PORT = 5006

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

filename="gambar.png"
size = os.stat(filename).st_size

fp = open('gambar.png','rb')
k = fp.read()
sent=0
for x in k:
   k_bytes = bytes([x])
   sock.sendto(k_bytes, (TARGET_IP, TARGET_PORT))
   sent = sent + 1
   print(k_bytes,f"terkirim {sent} of {size} ")