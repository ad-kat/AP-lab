# Function to count characters, words, and lines in a file
def count_characters_words_lines(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            
            # Count characters
            character_count = len(text)
            
            # Count words
            words = text.split()
            word_count = len(words)
            
            # Count lines
            lines = text.splitlines()
            line_count = len(lines)
            
            return character_count, word_count, line_count
    except FileNotFoundError:
        return None  # File not found
    except Exception as e:
        return str(e)  # Handle other exceptions

# Input file name
filename = "sample.txt"  # Replace with the path to your file

# Call the function and get counts
result = count_characters_words_lines(filename)
# Function to calculate total number of characters, words, and lines in a file
def count_chars_words_lines(filename):
    with open(filename, 'r') as file:
        content = file.read()
        char_count = len(content)
        word_count = len(content.split())
        line_count = len(content.splitlines())

    return char_count, word_count, line_count

# Get the filename from the user
filename = input("Enter the filename: ")

try:
    # Call the function and get the counts
    char_count, word_count, line_count = count_chars_words_lines(filename)

    # Print the results
    print("Total number of characters:", char_count)
    print("Total number of words:", word_count)
    print("Total number of lines:", line_count)

except FileNotFoundError:
    print("File not found. Please check the filename and try again.")
except Exception as e:
    print("An error occurred:", str(e))

# Check if the file exists
if result is None:
    print("File not found.")
else:
    character_count, word_count, line_count = result
    print(f"Total Characters: {character_count}")
    print(f"Total Words: {word_count}")
    print(f"Total Lines: {line_count}")
