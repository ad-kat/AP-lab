n = int(input("enter n -->"))
m = int(input("enter m -->"))
for n in range(n, m+1):
    c = 0
    for i in range(1, n+1):
        if n % i == 0:
            c += 1
    if c == 2:
        print(n, end=" ")
        c = 0
