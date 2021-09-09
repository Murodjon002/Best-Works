def func_digits_list(data):
    list1=[]
    list2=[]
    for i,v in data.items():
        list1.append(i)
        list2.append(v)
    return list1,list2
a,b=func_digits_list({1:"apple",
2:"limon",
3:"banana",
4:"charry"})
print(a,b,sep='\n')
