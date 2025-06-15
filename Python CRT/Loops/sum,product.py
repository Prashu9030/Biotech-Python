a,b=map(int,input().split())
n=int(input())
c=0
d=1
while a<=b:
    if(a%n==0):
       c=c+a
       d=d*a
    a=a+1
print(c)
print(d)
print(abs(c-d))
