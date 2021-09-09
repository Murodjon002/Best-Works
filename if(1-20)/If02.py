a=int(input())
b=int(input())
c=int(input())
if a>b:
    if b>c:
        print(b)
    else:
        if a>c:
            print(c)
        else:
            print(a)
else:
    if a>c:
        print(a)
    else:
        if b>c:
            print(c)
        else:
            print(b)