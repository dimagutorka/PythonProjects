import socket
import threading


# Define the function that handles client requests
def handle_client(client_socket):
	try:
		# Receive the client's request
		request = client_socket.recv(1024).decode('utf-8')
		print(f"Received request:\n{request}")

		# Send a simple HTTP response
		http_response = "HTTP/1.1 200 OK\r\n"
		http_response += "Content-Type: text/plain\r\n"
		http_response += "\r\n"
		http_response += "Hello from the server! This is a multi-threaded response.\r\n"

		client_socket.sendall(http_response.encode('utf-8'))
	except Exception as e:
		print(f"Error handling client: {e}")
	finally:
		# Close the connection
		client_socket.close()


def start_server(host='0.0.0.0', port=8080):
	# Create a socket object
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Bind the socket to the address and port
	server_socket.bind((host, port))

	# Start listening for connections
	server_socket.listen(5)
	print(f"Server is listening on {host}:{port}...")

	while True:
		# Accept incoming client connections
		client_socket, addr = server_socket.accept()
		print(f"Accepted connection from {addr}")

		# Create a new thread to handle the client's request
		client_handler = threading.Thread(target=handle_client, args=(client_socket,))
		client_handler.start()


if __name__ == "__main__":
	start_server()
