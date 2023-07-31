n = int(input("enter number-->"))
nn = n
ss = 0


while nn != 0:
    d = nn % 10
    nn = int(nn / 10)
    d3 = d ** 3
    ss = ss + d3

print(ss)
if ss == n:
    print("Armstrong")
else:
    print("not so")
