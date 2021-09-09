def func(N):
    sum=0
    for i in range(1,N+1):
        sum+=1/i
    return sum
print(func(int(input())))