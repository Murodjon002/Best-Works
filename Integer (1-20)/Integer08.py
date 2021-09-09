from math import sqrt
x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
x3=float(input())
y3=float(input())
a=sqrt(pow((x1-x2),2)+pow((y1-y2),2))
b=sqrt(pow((x3-x2),2)+pow((y3-y2),2))
c=sqrt(pow((x1-x3),2)+pow((y1-y3),2))
P=a+b+c
p=P/2
S=sqrt(p*(p-a)*(p-b)*(p-c))
print(round(P,2),round(S,2))