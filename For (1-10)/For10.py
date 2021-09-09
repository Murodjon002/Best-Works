def func(A,N):
    sum=0
    for i in range(N+1):
        sum+=A**i
    return sum
print(func(float(input()),int(input())))