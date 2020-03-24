import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port_num = 8888
server_address = ('127.0.0.1', port_num)
print("Connecting to Server: 127.0.0.1" , " Port:", port_num)
sock.connect(server_address)
try:
    filename="tulisan1.txt"
    filetemp = open(filename,"rb")
    file = filetemp.read(4096)
    filetemp.close()
    file = file.decode()

    message = "add "+filename+" "+file
    sock.send(message.encode())
    print("adding...")
    data = sock.recv(4096).decode()
    print(data)

finally:
    print("Closing Connection")
    sock.close()