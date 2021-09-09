def func(price):
    list1=[]
    for i in range(1,11):
        list1.append(price*i)

    return list1
print(func(float(input())))