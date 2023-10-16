import socket

def search_number(numbers, search_value):
    return search_value in numbers

def sort_numbers(numbers, ascending=True):
    return sorted(numbers) if ascending else sorted(numbers, reverse=True)

def split_numbers(numbers):
    odd_numbers = [x for x in numbers if x % 2 != 0]
    even_numbers = [x for x in numbers if x % 2 == 0]
    return odd_numbers, even_numbers

def main():
    host = "127.0.0.1"
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Server is ready to receive data...")

    while True:
        client_socket, addr = server_socket.accept()
        print("Connection from:", addr)

        data = client_socket.recv(1024).decode()
        if data.lower() == "exit":
            print("Server stopping...")
            break

        data = data.split(" ")
        choice = int(data[0])
        numbers = [int(x) for x in data[1:]]

        result = None

        if choice == 1:
            search_value = int(input("Enter the number to search for: "))
            result = search_number(numbers, search_value)
        elif choice == 2:
            ascending = input("Sort in ascending order? (y/n): ").lower() == 'y'
            result = sort_numbers(numbers, ascending)
        elif choice == 3:
            odd_numbers, even_numbers = split_numbers(numbers)
            result = {"odd_numbers": odd_numbers, "even_numbers": even_numbers}

        client_socket.send(str(result).encode())
        client_socket.close()

    server_socket.close()

if __name__ == "__main__":
    main()
