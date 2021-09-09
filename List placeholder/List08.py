def func(n):
    list1=[]
    for i in range(1,n+1):
        list1.append(i)
    k=0
    while n-1>k:

        list1[k]=int(list1[k])
        k+=1
        list1[k]=float(list1[k])
        k+=1

    
    return list1
print(func(int(input())))