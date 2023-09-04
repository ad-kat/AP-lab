import time

# Get the user name from the user
username = input("Enter your username: ")

# Get the current time
current_time = time.localtime()

# Print a greeting message
if current_time.tm_hour < 12:
    print("Good morning,", username)
elif current_time.tm_hour < 18:
    print("Good afternoon,", username)
else:
    print("Good evening,", username)
