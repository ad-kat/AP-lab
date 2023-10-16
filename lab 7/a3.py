import sys
import textwrap

def wrap_text(filename, width):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            wrapped_text = textwrap.fill(text, width)

        print(wrapped_text)
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python wrap.py <filename> <width>")
    else:
        filename = sys.argv[1]
        width = int(sys.argv[2])
        wrap_text(filename, width)
