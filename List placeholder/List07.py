def func(n,k):
    list1=[]
    for i in range(k,2*n-1+k,2):
        list1.append(i)

    return list1

print(func(int(input()),int(input())))