#LCM of two numbers
def rlcm(a,b,x,y):
    if(a==b):
        return (x*y)//a
    if(a>b):
        return rlcm(a-b,b,x,y) #recursive call-1
    else:
        return rlcm(a,b-a,x,y) #recursive call-2
a,b=map(int,input().split())
ans=rlcm(a,b,a,b)
print(ans)
print()