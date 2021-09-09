a=int(input())
m=0
if a>=1 and a<=9:
    if a%2==1:
        m+=a
elif a>=10 and a<=99:
    if a//10%2==1:
        m+=a//10
    if a%10%2==1:
        m+=a%10
elif a>=100 and a<=999:
    if a//100%2==1:
        m+=a//100
    if a//10%10%2==1:
        m+=a//10%10
    if a%10%2==1:
        m+=a%10

elif a>=1000 and a<=9999:
    if a//1000%2==1:
        m+=a//1000
    if a//100%10%2==1:
        m+=a//100%10
    if a//10%10%2==1:
        m+=a//10%10
    if a%10%2==1:
        m+=a%10
print(m)