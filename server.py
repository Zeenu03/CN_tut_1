import socket
import time

HOST = '127.0.0.1'  # Localhost
PORT = 12345        # Port to listen on

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))  # Bind to the specified host and port
server_socket.listen(1)  # Allow only 1 client at a time

print(f"Single-Process Server listening on {HOST}:{PORT}")

while True:
    conn, addr = server_socket.accept()  # Accept a client connection
    print(f"Connected by {addr}")

    data = conn.recv(1024)  # Receive data from the client
    if not data:
        break

    time.sleep(3)  # Introduce a 3-second delay
    reversed_data = data.decode()[::-1]  # Reverse the string
    conn.sendall(reversed_data.encode())  # Send the reversed string back

    conn.close()  # Close the connection
    print(f"Connection with {addr} closed")
