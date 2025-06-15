a,b=map(int,input().split())
c=0
while (a<=b):
    if (a%5==0 and a%3==0):
        c=c+a
    a=a+1
print(c)
