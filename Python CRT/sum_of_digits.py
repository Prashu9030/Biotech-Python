n=int(input())
sd=0
while n!=0:
    r=n%10
    sd+=r
    n=n//10
    if(n==0 and sd>9):
        n=sd
        sd=0
print(sd)