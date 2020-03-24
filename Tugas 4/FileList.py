import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 8888)
print("Connecting to Server: 127.0.0.1 Port: 8888")
sock.connect(server_address)

try:
    message = "list "
    sock.send(message.encode())
    print("Request sent")
    data = sock.recv(4096)
    print(data.decode())
finally:
    sock.close()