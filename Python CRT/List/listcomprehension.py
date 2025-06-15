x = int(input())
y = int(input())
z = int(input())
n = int(input())
a=0
b=0
c=0
if(x==0 and y==0 and z==0):
    print('[]')
else:
    print('[',end="")
    for a in range(x+1):
        for b in range(y+1):
            for c in range(z+1):
                if a+b+c!=n:
                    print([a,b,c],end="")
                    if(a==x and b==y and c==z):
                        print(end="]")
                    else:
                        print(', ',end="")
                c+=a
            b+=c
        a+=b