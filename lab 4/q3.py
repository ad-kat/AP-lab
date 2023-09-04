import os

# List all the environment variables
for variable in os.environ:
    print(variable, os.environ[variable])
