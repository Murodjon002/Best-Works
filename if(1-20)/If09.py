Temp=int(input())
if Temp<0:
    print("Freezing")
elif Temp>=1 and Temp<=10:
    print("Very Cold")
elif Temp>=11 and Temp<=20:
    print("Cold")
elif Temp>=21 and Temp<=30:
    print("Normal")
elif Temp>=31 and Temp<=40:
    print("Hot")
else:
    print("Very Hot")