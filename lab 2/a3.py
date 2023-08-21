def create_text_file():
  """
  Creates a text file with minimum eight lines.
  """
  with open("text.txt", "w") as f:
    f.write("This is the first line.\n")
    f.write("This is the second line.\n")
    f.write("This is the third line.\n")
    f.write("This is the fourth line.\n")
    f.write("This is the fifth line.\n")
    f.write("This is the sixth line.\n")
    f.write("This is the seventh line.\n")
    f.write("This is the eighth line.\n")

def read_data_from_file():
  """
  Reads data from the file.
  """
  with open("text.txt", "r") as f:
    data = f.readlines()
  return data

def store_data_in_dictionary(data):
  """
  Stores data in dictionary form considering line numbers as keys,string and total length of the string as values. Values is of type list.Print the resultant dictionary.
  """
  dictionary = {}
  for i, line in enumerate(data):
    dictionary[i] = [line, len(line)]
  return dictionary

def create_dictionary_from_file(data):
  """
  Creates a dictionary from the file, considering letters represented as keys and frequencies of letters as values . Print the dictionary.
  """
  dictionary = {}
  for line in data:
    for letter in line:
      if letter in dictionary:
        dictionary[letter] += 1
      else:
        dictionary[letter] = 1
  return dictionary


create_text_file()
data = read_data_from_file()
dictionary = store_data_in_dictionary(data)
print(dictionary)
dictionary = create_dictionary_from_file(data)
print(dictionary)
