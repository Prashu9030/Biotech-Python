x,y=map(int,input().split())
if(x>0 and y>0):
    print("quadrant1")
if(x>0 and y<0):
    print("q2")
if(x<0 and y<0):
    print("q3")
if(x<0 and y>0):
    print("q4")
if(x==0 and y==0):
    print("origin")
if(x==0 and y!=0):
    print("Y-axis")
if(x!=0 and y==0):
    print("X-axis")
