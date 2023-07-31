n = int(input("enter n"))
print("part 1:")
print("now enter n strings")
ll = []
for i in range(1, n+1):
    inp = input("-->")
    ll.append(inp)

print("part 2:")
c = 0
for word in ll:
    if word[0] == word[-1]:
        if len(word) > 1:
            c += 1
print(c)
print("part 3:")

for word in ll:
    if len(word) % 2 == 1:
        print(word, end=" ")
    print()



