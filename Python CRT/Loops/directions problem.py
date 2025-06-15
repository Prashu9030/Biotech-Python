e,n,w,s=map(int,input().split())
x=e-w
y=n-s
if(x>0 and y>0):
    print("NE")
if(x>0 and y<0):
    print("NW")
if(x<0 and y<0):
    print("SW")
if(x<0 and y>0):
    print("SE")
if(x==0 and y<0):
    print("South")
if(x==0 and y>0):
    print("North")
if(x>0 and y==0):
    print("East")
if(x<0 and y==0):
    print("West")
