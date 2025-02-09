import socket
import time
import threading

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    
    data = conn.recv(1024).decode()
    if data:
        time.sleep(3)  # Simulate processing delay
        response = data[::-1]  # Reverse the string
        conn.sendall(response.encode())
    
    conn.close()
    print(f"Client {addr} disconnected.")

def main():
    host = '127.0.0.1'  # Localhost
    port = 65433  # Port number
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  # Allow multiple clients to queue
    
    print("Multi-Threaded Server is listening for connections...")
    
    while True:
        conn, addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    main()
