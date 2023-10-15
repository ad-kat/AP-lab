# Function to print lines of a file in reverse order
def print_lines_in_reverse(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    for line in reversed(lines):
        print(line.strip())

# Get the filename from the user
filename = input("Enter the filename: ")

try:
    # Call the function to print lines in reverse order
    print_lines_in_reverse(filename)

except FileNotFoundError:
    print("File not found. Please check the filename and try again.")
except Exception as e:
    print("An error occurred:", str(e))
