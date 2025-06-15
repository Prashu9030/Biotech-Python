str=input("enter your password")
num=0
spe=0
cap=0
for i in range(0,len(password)):
    if password[i].isalpha():
        cap+=1
    elif st[i].isnumerics():
        num=+1
    else:
        spe=+1
if spe!=0 and num!=0 and cap!=0:
    print("it is valid password")
else:
    print("it is not valid password")
