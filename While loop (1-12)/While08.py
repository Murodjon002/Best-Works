n=int(input())
k=int(input())
list1=[]
while k>n:
    if n%2==1:
        list1.append(n)
    n+=1
print(list1)