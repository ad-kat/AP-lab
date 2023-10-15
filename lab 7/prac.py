filename = input("-->")
try:
    with open(filename, 'r') as file:
        # Step 3: Print contents of the file
        print("Contents of the file:")
        print(file.read())

    # Step 4: Append words or phrases to the file (to be entered by the user)
    additional_content = input("Enter words or phrases to append to the file (or press Enter to skip): ")
    if additional_content:
        with open(filename, 'a') as file:
            file.write('\n' + additional_content)

    print("File updated successfully!")

except FileNotFoundError:
    print("File not found. Please check the filename and try again.")
except Exception as e:
    print("An error occurred:", str(e))
