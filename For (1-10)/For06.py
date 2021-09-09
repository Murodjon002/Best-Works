def func_list(A,B):
    sum=0
    for i in range(A,B):
        sum+=i
    return sum
print(func_list(int(input()),int(input())))