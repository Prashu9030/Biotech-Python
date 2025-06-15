n=int(input())
ans=1
while n>0:
    r=n510
    n=n//10
    if(r==0):
        continue
    ans=ans*r
print(ans)
