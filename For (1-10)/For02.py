def func_str(N):
    list1=[]
    for i in range(N):
        list1.append(i)
    str1=str(list1)
    return str1[1:-1]
print(func_str(int(input())))