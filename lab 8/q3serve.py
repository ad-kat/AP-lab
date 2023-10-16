import socket

def is_palindrome(string):
    # Remove spaces and convert to lowercase
    string = string.replace(" ", "").lower()
    return string == string[::-1]

def count_vowels(string):
    vowels = "aeiouAEIOU"
    return {vowel: string.count(vowel) for vowel in vowels}

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
        if data.lower() == "stop":
            print("Server stopping...")
            break

        is_palindrome_result = is_palindrome(data)
        vowel_count = count_vowels(data)

        response = f"Palindrome: {is_palindrome_result}\nLength: {len(data)}\nVowel Count: {vowel_count}"

        client_socket.send(response.encode())
        client_socket.close()

    server_socket.close()

if __name__ == "__main__":
    main()
