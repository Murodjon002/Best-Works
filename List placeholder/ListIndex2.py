def func(L1):
    first_iteam=L1[0]
    last_iteam=L1[-1]
    return first_iteam,last_iteam
a,b=func(input().split(","))
print(int(a),int(b))