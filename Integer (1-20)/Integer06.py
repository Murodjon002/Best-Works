from math import sqrt,pow
r=int(input())
n=int(input())
a=int(input())
b=int(input())
sum=(pow(1+r/100,n))/(sqrt(a*a+b*b))
print(sum)