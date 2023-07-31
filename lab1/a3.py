inp = input("Enter a string: ")
flag = 0
for character in inp:
    if not character.isdigit() and character not in "ABCDEFabcdef":
        flag += 1
if flag == 0:
    print("hexadecimal number")
else:
    print("not so")
