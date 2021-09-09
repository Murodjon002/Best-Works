def func(n):
    list1=[]
    k=0
    for i in range(n):
        list1.append(i)
        list1[k]=float(list1[k])
        k+=1
    return list1
print(func(int(input())))