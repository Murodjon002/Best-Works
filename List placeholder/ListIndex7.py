def func(L1,n,k):
    m=0
    while len(L1)>m:
        L1[m]=int(L1[m])
        m+=1
    return L1[n:k]
print(func(input().split(","),int(input()),int(input())))