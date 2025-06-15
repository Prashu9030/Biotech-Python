i=int(input())
if(i%8==0):
    print("SU")
if(i%8==7):
    print("SL")
if(i%8==1 or i%8==4):
    print("L")
if(i%8==2 or i%8==5):
    print("M")
if(i%8==3 or i%8==6):
    print("U")
