n=int(input())
c=0
while n>0:
    r=n%10
    n=n//10
    c=c+r
print(c)
