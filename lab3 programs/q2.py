def the_func():
    print("enter ints for list.Enter -999 to stop")
    n = int(input("-->"))
    new_l=[]
    the_list=[]
    while n != -999:
        the_list.append(n)
        n=int(input("-->"))
    for i in the_list:
        if i not in new_l:
            new_l.append(i)
        else:
            continue
    return new_l


print(the_func())
