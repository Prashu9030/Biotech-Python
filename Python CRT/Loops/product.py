n=int(input())
c=1
while n>0:
    r=n%10
    n=n//10
    if(r==0):
        continue
    c=c*r
print(c)
