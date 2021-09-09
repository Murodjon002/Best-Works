f=open("txt_file/data07.txt").read()
list1=0
for i in f:
    if i=="0" or i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9":
        list1+=int(i)
print(list1)