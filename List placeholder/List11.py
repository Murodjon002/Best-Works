def func(n):
    list1=[]
    m=1
    s=0
    while n>s:
        list1.append(m)
        m*=2
        s+=1
    return list1[::-1]
print(func(int(input())))