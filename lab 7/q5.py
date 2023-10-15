import re

# Function to check if a string starts and ends with the same character
def starts_and_ends_with_same_char(input_string):
    # Define a regular expression pattern to match the condition
    pattern = r'^(.).*\1$'
    return bool(re.match(pattern, input_string))

# Input string to test
input_string = input("Enter a string: ")

if starts_and_ends_with_same_char(input_string):
    print(f"The string '{input_string}' starts and ends with the same character.")
else:
    print(f"The string '{input_string}' does not start and end with the same character.")

