n=int(input())
ans=0
while n>0:
    r=n%10
    ans=ans*10+r
    n=n//10
print(ans)
