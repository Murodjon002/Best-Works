f=open("txt_file/data09.txt").read()
list1=[]

for i in f:
    if i=="0" or i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9":
        list1.append(int(i))
m=list1[0]
for k in list1:
    if m>k:
        
        m=k
print(m)