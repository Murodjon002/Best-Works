def add_two_list(a,b):
    add=a+b
    list1=[]
    k=0
    while len(add)>k:
        list1.append(add[k])
        k+=1


    
    return list1
print(add_two_list(input(),input()))