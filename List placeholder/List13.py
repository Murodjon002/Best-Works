def func(n,k):
    list1=[]
    l=0
    for i in range(k,n*k+1,k):
        list1.append(i)
        list1[l]=float(list1[l])
        l+=1
    return list1
print(func(int(input()),int(input())))