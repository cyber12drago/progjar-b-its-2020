import socket

TARGET_IP = "127.0.0.1"
TARGET_PORT = 5006

mytext="YugiYukiYuseiYumaYuyaYusaku"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes(mytext.encode()),(TARGET_IP,TARGET_PORT))