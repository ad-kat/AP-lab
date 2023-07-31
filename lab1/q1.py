l1 = []
l2 = []
print("Enter numbers for list 1.Enter -1 to exit")
d1 = 0
d2 = 0
while d1 == 0:
    n = int(input("->"))
    if n == -1:
        d1 = 1
    else:
        l1.append(n)

print("Enter numbers for list 2.Enter -1 to exit")
while d2 == 0:
    n = int(input("->"))
    if n == -1:
        d2 = 1
    else:
        l2.append(n)

lf = []
for x in l1:
    if x % 2 == 1:
        lf.append(x)
for x in l2:
    if x % 2 == 0:
        lf.append(x)

print(lf)

