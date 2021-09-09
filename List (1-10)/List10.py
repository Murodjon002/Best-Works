def revers_add_list(a):
    list1=[]
    k=0
    while len(a)>k:
        list1.append(a[k])
        k+=1
    
    return list1+list1
print(revers_add_list(input()))