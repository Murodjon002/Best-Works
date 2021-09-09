n=int(input())
list1=[]
x=n%10
m=0
k=len(str(n))-1
while k>m:
    n//=10
    m+=1
print(n+x)

    
