def the_func():
    print("enter ints for list.Enter -999 to stop")
    n = int(input("-->"))
    r=1
    the_list=[]
    while n != -999:
        the_list.append(n)
        n=int(input("-->"))
    for num in the_list:
        r = r * num
    return r


print(the_func())


