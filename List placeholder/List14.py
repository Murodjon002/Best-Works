def func(n):
    list1=[]
    while n!=0:
        x=n%10
        list1.append(x)
        n//=10
        
    return list1[::-1]
print(func(int(input())))