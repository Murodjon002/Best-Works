a=int(input())
if a>=1 and a<=9:
    print(a)
elif a>=10 and a<=99:
    print(a//10+a%10)
elif a>=100 and a<=999:
    print(a//100 +a//10%10+a%10)
elif a>=1000 and a<=9999:
    print(a//1000+a//100%10+a//10%10+a%10)