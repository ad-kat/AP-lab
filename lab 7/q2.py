# Function to count occurrences of each word in a file
def count_word_occurrences(filename):
    word_count = {}
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()

        for word in words:
            # Remove punctuation and convert to lowercase for accurate counting
            cleaned_word = word.strip('.,!?()[]{}"\'').lower()
            word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1

    return word_count

# Sample input: Creating a sample text file
with open('sample_file.txt', 'w') as sample_file:
    sample_file.write("Hello world! This is a sample text file. Hello, world!")

# Get the filename from the user
filename = input("Enter the filename: ")
filename=open(filename,'r')

try:
    # Call the function to get word occurrences
    word_occurrences = count_word_occurrences(filename)

    # Print the word occurrences
    print("Word occurrences in the file:")
    for word, count in word_occurrences.items():
        print(f"'{word}': {count}")

except FileNotFoundError:
    print("File not found. Please check the filename and try again.")
except Exception as e:
    print("An error occurred:", str(e))
