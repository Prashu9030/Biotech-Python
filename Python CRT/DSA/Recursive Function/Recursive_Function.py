#write a recursive program to print the numbers from a to b where,a=low value and b=high value
#Input-5,10 Output-5,6,7,8,9,10

#NON_RECURSIVE PROGRAM
a,b=map(int,input().split())
while a<=b:
    print(a)
    a+=1
print()

#RECURSIVE PROGRAM
def rlh(x,y):
    if(x<=y):
        print(x)
        x+=1
        rlh(x,y)
a,b=map(int,input().split())
rlh(a,b)#calling function