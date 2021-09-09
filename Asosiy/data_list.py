f=open("data.json").read().split("\n")[1:-1]
list1=[]
list2=[]
for i in f:
    list1.append(i.split(":")[0].strip('" "'))
    list2.append(float(i.split(":")[1].strip(',').strip('" "')))

print(list1)
print(list2)




