def func_list(A,B):
    list1=[]
    for i in range(A,B+1):
        list1.append(i)

    return list1
print(func_list(int(input()),int(input())))