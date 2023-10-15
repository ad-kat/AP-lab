import re

# Function to validate an email address
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

# Read email addresses from input.txt
try:
    with open('input.txt', 'r') as input_file:
        email_list = input_file.read().splitlines()
except FileNotFoundError:
    print("Input file 'input.txt' not found.")
    exit()

valid_emails = []
invalid_emails = []

# Separate valid and invalid email addresses
for email in email_list:
    if is_valid_email(email):
        valid_emails.append(email)
    else:
        invalid_emails.append(email)

# Write valid emails to valid.txt
with open('valid.txt', 'w') as valid_file:
    for email in valid_emails:
        valid_file.write(email + '\n')

# Write invalid emails to invalid.txt
with open('invalid.txt', 'w') as invalid_file:
    for email in invalid_emails:
        invalid_file.write(email + '\n')

print(f"Valid email addresses written to 'valid.txt': {len(valid_emails)}")
print(f"Invalid email addresses written to 'invalid.txt': {len(invalid_emails)}")
