import socket

def main():
    host = "127.0.0.1"
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        user_input = input("Enter a string (or 'Stop' to quit): ")
        client_socket.send(user_input.encode())

        if user_input.lower() == "stop":
            print("Client stopping...")
            break

        response = client_socket.recv(1024).decode()
        print("Server Response:")
        print(response)

    client_socket.close()

if __name__ == "__main__":
    main()
