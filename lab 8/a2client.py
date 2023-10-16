import socket

def main():
    host = "127.0.0.1"
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        print("\nOptions:")
        print("1. Search for a number")
        print("2. Sort the set")
        print("3. Split odd and even numbers")
        print("4. Exit")

        choice = int(input("Enter your choice: "))
        client_socket.send(str(choice).encode())

        if choice == 4:
            print("Client stopping...")
            client_socket.send("exit".encode())
            break

        numbers = input("Enter a set of integers separated by spaces: ")
        client_socket.send(numbers.encode())

        result = client_socket.recv(1024).decode()
        print("Server Response:")
        print(result)

    client_socket.close()

if __name__ == "__main__":
    main()
