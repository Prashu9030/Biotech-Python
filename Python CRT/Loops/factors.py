n=int(input())
a=1
c=0
while a<=n:
    if (n%a==0):
        print(a,end=" ")
    c+=1
    a=a+1
print("No of factors",c)
        
    
