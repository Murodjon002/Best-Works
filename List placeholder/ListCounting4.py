def fun(n):
    max=int(n[0])
    index=0
  
    k=0
    while len(n)>k:
        n[k]=int(n[k])
        if n[k]>max:
            max=n[k]
            index=k
        k+=1
        

    return index
a=fun(input().split(","))
print(int(a))