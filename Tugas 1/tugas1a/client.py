import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 31000)
print ("connecting to",server_address, end="...")
filename = "send.txt"
file_open = open(filename, "rb")
sock.connect(server_address)

try:
    # Send data
    file_read = file_open.read()
    print ("sending", file_read)
    sock.sendall(file_read)
finally:
    print ('closing socket...')
    sock.close()
