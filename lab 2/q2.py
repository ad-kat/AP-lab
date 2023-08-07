r1 = int(input("enter order of 1st matrix:"))
r2 = int(input("enter order of 2nd matrix:"))
l1 = []
l2 = []
print("enter elements for 1st matrix:")
for i in range(0, r1):
    lb = []
    for j in range(0, r1):
        lb.append(int(input("-->")))
    l1.append(lb)
mat1 = {}
r = 0
for i in l1:
    c = 0
    lb = {}
    for j in l1[r]:
        lb[c] = j
        c += 1
    c = 0
    mat1[r] = lb
    r += 1
print("enter elements for 2nd matrix:")
for i in range(0, r2):
    lb = []
    for j in range(0, r2):
        lb.append(int(input("-->")))
    l2.append(lb)
mat2 = {}
r = 0
for i in l2:
    c = 0
    lb = {}
    for j in l2[r]:
        lb[c] = j
        c += 1
    c = 0
    mat2[r] = lb
    r += 1
sum={}

if r1 != r2:
    print("Addition not possible")
else:

    for i in range(0,r1):
        sum[i] = {}
        for j in range(0,r2):
            sum[i][j] = mat1[i][j] + mat2[i][j]

    for i in range(0,r1):
        print()
        for j in range(0,r2):
            print(sum[i][j], end=" ")





