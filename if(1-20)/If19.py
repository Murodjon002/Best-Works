a=int(input())
x=a//10000
y=a//1000%10
z=a//100%10
l=a//10%10
k=a%10
m=x 
if m<y:
    m=y
if m<z:
    m=z
if m<l:
    m=l
if m<k:
    m=k
print(m)