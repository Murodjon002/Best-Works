def func_list(N):
    list1=[]
    for i in range(N):
        list1.append(i)

    return list1[1::2]
print(func_list(int(input())))