def fun(n):
    max=int(n[0])
    min=int(n[0])
    k=0
    while len(n)>k:
        n[k]=int(n[k])
        if n[k]>max:
            max=n[k]
        if n[k]<min:
            min=n[k]
        k+=1

    return min,max
a,b=fun(input().split(","))
print(int(a),int(b))