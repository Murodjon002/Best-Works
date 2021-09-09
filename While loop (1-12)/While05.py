n=int(input())
k=int(input())
sum=0
while n<k:
    if n%2==1:
        sum+=n
    n+=1
   
print(sum)
