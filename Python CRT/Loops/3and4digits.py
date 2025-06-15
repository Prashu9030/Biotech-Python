n=int(input("enter the Integer Value :"))
if((n>=100 and n<=999) or (n<=-100 and n>=-999)):
    print(f"{n} is a Three digit number")
else:
    print(f"{n} is not a three digit number")
if((n>999 and n<=9999) or (n<-999 and n>=-9999)):
    print(f"{n} is a four digit number")
else:
    print(f"{n} is not a four digit number")