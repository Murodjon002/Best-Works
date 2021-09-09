def func(n):
    list1=[]
    for i in range(n):
        list1.append(i)
    k=0
    while n-1>k:
        
        list1[k]=str(list1[k])
        k+=1
        list1[k]=int(list1[k])


    return list1

print(func(int(input())))