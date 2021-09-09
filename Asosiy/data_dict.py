import json
f=open('data.json')
list1=[]
list2=[]
a=json.load(f)
for i in a:
    list1.append(i)
    list2.append(float(a[i]))
print(list1)
print(list2)