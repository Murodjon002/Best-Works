def func(n):
   
    n[-4]=int(n[-4])
    n[-3]=int(n[-3])
    n[-2]=int(n[-2])
    n[-1]=int(n[-1])
    return n[-4:]

print(func(input().split(",")))