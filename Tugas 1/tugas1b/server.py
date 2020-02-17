import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 31000)
print(f"starting up on {server_address}")
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)

while True:
	print("waiting for a connection")
	connection, client_address = sock.accept()
	print(f"connection from {client_address}")
	# Receive the data in small chunks and retransmit it
	data = connection.recv(512)
	file_open = open(data.decode(), 'rb')
	file_read = file_open.read()
	connection.sendall(file_read)
	file_open.close()
	print("request sent.")
	# Clean up the connection
	connection.close()