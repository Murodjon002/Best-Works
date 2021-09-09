f=open("txt_file/data01.txt").read().split(",")
list1=[]
for i in f:
    list1.append(int(i))
print(list1)
