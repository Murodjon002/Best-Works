def func(L1):
    k=0
    while len(L1)>k:
        L1[k]=int(L1[k])
        k+=1
    return L1[::3]
print(func(input().split(",")))