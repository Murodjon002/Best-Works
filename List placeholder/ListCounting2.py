def func(L1):
    l=int(L1[0])
    k=0
    while len(L1)>k:
        L1[k]=int(L1[k])
        if l>int(L1[k]):
            l=int(L1[k])
        k+=1
        
            

    return l 
print(func(input().split(",")))