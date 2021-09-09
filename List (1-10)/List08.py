def find_item(a,n):
    list1=[]
    k=0
    while len(a)>k:
        list1.append(a[k])
        k+=1
    

    return a.find(n)
print(find_item(input(),input()))