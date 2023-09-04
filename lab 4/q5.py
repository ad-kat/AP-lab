# Accept a sentence from the user
import string
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Capitalize the first letter of each word
capitalized_words = [word.capitalize() for word in words]

# Join the capitalized words to form the modified sentence
capitalized_sentence = ' '.join(capitalized_words)

# Print the modified sentence
print("Modified Sentence:", capitalized_sentence)
