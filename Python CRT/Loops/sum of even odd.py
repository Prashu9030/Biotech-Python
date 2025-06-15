n=int(input())
a=0
b=0
while n>0:
    r=n%10
    n=n//10
    if(r%2==0):
        a=a+r
    else:
        b=b+r
print(abs(a-b))
