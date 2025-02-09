import socket
import sys

def main():
    host = '127.0.0.1'  # Server address
    port =  12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Read input from command-line argument or use a default value
    if len(sys.argv) > 1:
        message = sys.argv[1]
    else:
        message = "default_message"  # Default input if none is provided

    client_socket.sendall(message.encode())

    response = client_socket.recv(1024).decode()
    print(f"Reversed string from server: {response}")

    client_socket.close()

if __name__ == "__main__":
    main()
