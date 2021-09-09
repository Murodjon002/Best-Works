def func(L1,n):
    k=0
    while len(L1)>k:
        L1[k]=int(L1[k])
        k+=1
        return L1[::-n]

print(func(input().split(","),int(input())))