import socket

PORT = 65433
BUFFER_SIZE = 1024

def process_request(request):
    choice, input_data = request.split(":", 1)

    if choice == "1":
        return input_data.swapcase()
    elif choice == "2":
        try:
            return str(eval(input_data))  # WARNING: Eval can be insecure!
        except:
            return "Invalid expression"
    elif choice == "3":
        return input_data[::-1]
    else:
        return "Invalid choice"

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", PORT))
    server_socket.listen(1)  # Only one client at a time

    print(f"Single-Process Server listening on port {PORT}")

    while True:
        client_socket, _ = server_socket.accept()
        request = client_socket.recv(BUFFER_SIZE).decode()
        response = process_request(request)
        client_socket.send(response.encode())
        client_socket.close()

if _name_ == "_main_":
    main()