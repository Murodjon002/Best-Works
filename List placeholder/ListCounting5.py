def func(n):
    k=0
    list1=[]
    while len(n)>k:
        n[k]=int(n[k])
        
        if n[k]%2==0:
            list1.append(n[k])
        k+=1

    return list1

print(func(input().split(",")))