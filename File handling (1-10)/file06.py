f=open("txt_file/data06.txt").read().split("\n")
list1=[]
for i in f:
    list1.append(len(i))
print(list1)
