def extsort(file_list):
    return sorted(file_list, key=lambda x: x.split(".")[-1])

# Input a list of file names from the user
file_list = input("Enter a list of file names separated by spaces: ").split()

# Sort the list of files based on extension
sorted_files = extsort(file_list)

# Print the sorted list
print(sorted_files)
