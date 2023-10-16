# Open the file for reading
file_path = input("filename:")  # Replace with your file's path
try:
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Print each line in reverse order
    for line in reversed(lines):
        print(line.strip())  # Use strip() to remove newline characters
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
