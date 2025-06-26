#write a program to print the factorial of the number
#Input:3 #Output:6
#Non recursive program
n=int(input())
f=1
while n>=1:
    f*=n
    n-=1
print(f)
print()

#Recursive program from 1 to 5
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1) #recursive calling
n=int(input())
f=fact(n) #calling function
print(f)
print()
    
'''
n=4
return 4*fact(3)
-----------------
n=3
return 3*fact(2)
-----------------
n=2
return 2*fact(1)
-----------------
n=1
return 1
'''
#Recursive program from 5 to 1
def fact(x,n,a,b):
    if(x==a):
        print(b)
    else:
        n-=1
        a+=1
        return fact(x,n,a,b*n)
n=int(input())
if(n==0 or n==1):
    print(1)
else:
    fact(n,1,n)