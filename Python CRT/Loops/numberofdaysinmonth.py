Month=int(input("enter the month number"))
if(Month==1 or Month==3 or Month==5 or Month==7 or Month==8 or Month==10 or Month==12):
    print("31 days.....!")
elif(Month==4 or Month==6 or Month==9 or Month==11):
    print("30 days....,!")
elif(Month==2):
    print("28 days or 29 days.....!")
else:
    print("In-Valid Month")