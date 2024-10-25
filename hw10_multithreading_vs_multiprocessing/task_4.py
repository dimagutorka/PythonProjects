import socket
import threading
from typing import Tuple


def handle_client(client_socket: socket.socket) -> None:
    """
    Handles the client's request and sends a simple HTTP response.

    Args:
        client_socket (socket.socket): The socket connected to the client.

    This function receives data from the client, prints the HTTP request,
    and responds with a simple HTTP 200 message. It ensures the socket
    is closed after handling the request.
    """
    try:
        # Receive data from the client
        request = client_socket.recv(1024).decode('utf-8')
        print(f"Received request:\n{request}")

        # Prepare and send a simple HTTP response
        http_response = "HTTP/1.1 200 OK\r\n"
        http_response += "Content-Type: text/plain; charset=utf-8\r\n\r\n"
        http_response += "Hello from the server! This is a multi-threaded response.\r\n"

        client_socket.sendall(http_response.encode('utf-8'))
    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        # Close the client socket
        client_socket.close()


def start_server(host: str = '0.0.0.0', port: int = 8080) -> None:
    """
    Starts a multi-threaded TCP server.

    Args:
        host (str): The host IP address to bind the server to. Defaults to '0.0.0.0' for all interfaces.
        port (int): The port number on which the server listens for incoming connections.

    This function sets up a TCP server that listens for incoming connections. For each client,
    it creates a new thread to handle the connection, allowing multiple clients to connect
    simultaneously without blocking the main server loop.
    """
    # Create a socket using IPv4 (AF_INET) and TCP (SOCK_STREAM)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the specified host and port
    server_socket.bind((host, port))
    # Start listening for incoming connections (up to 5 clients can be queued)
    server_socket.listen(5)
    print(f"Server is listening on {host}:{port}")

    while True:
        # Accept incoming client connections
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")

        # Create a new thread to handle the client's request
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()


if __name__ == "__main__":
    start_server()
