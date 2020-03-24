import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 8888)
print("Connecting to Server: 127.0.0.1 Port: 8888")
sock.connect(server_address)

try:
    namafile = "tulisan2.txt"
    message = "download " + namafile
    print("Requesting File",namafile,"to Server")
    sock.send(message.encode())

    filedata = sock.recv(4096)
    filetemp = open(namafile, "wb")
    filetemp.write(filedata)
    filetemp.close()

    print("File has been Received")
finally:
    print("Closing Connection")
sock.close()