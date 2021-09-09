def func(n):
    a=[]
    for i in range(2,2*n+1,2):
        a.append(i)
    return a
print(func(int(input())))