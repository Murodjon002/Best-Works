a=int(input())
x=a//10000
y=a//1000%10
z=a//100%10
l=a//10%10
k=a%10
m=x 
count=5
if m<y:
    count=4
    m=y
if m<z:
    count=3
    m=z
if m<l:
    count=2
    m=l
if m<k:
    count=1
    m=k
print(m,count)