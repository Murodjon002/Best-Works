f=open("txt_file/data05.txt").read()
list1=[]
list2=[]
for i in f:
    if i=="0" or i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9":
        list1.append(i)
    else:
        list2.append(i)
print(len(list1),len(list2))
