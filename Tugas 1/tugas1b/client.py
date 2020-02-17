import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 31000)
namafile = "image.jpg"

print ("Connecting to", server_address)
sock.connect(server_address)

try:
    # Send data
    print("Sending",namafile)
    sock.sendall(namafile.encode())
    #Look for Response
    while True:
        data = sock.recv(512)
        received = open("image2.jpg",'a+b')
        if not data:
            received.close()
            break
        received.write(data)
        print ("File received",data)
finally:
    print ('closing socket')
    sock.close()
