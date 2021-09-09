a=int(input())
result=""
if a==0:
    print("son 0 ga teng")
else:
    if a>0:
        result+="musbat"
    else:
        result+="manfiy"
    if a%2==0:
        result+=" juft son"
    else:
        result+=" toq son"
print(result)
