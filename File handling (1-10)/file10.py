f=open("txt_file/data10.txt").read().split("\n")
m=len(f[0])
for i in f:
    if len(i)>m:
        m=len(i)
print(m)
    


