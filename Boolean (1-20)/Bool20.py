a=int(input())
x=a//10000
y=a//1000%10
z=a//100%10
k=a//10%10
l=a%10
print(x<y and y<z and z<k and k<l)