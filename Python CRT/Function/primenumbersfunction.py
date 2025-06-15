#Method 1
def num(n):
    count=0
    for i in range(1,n+1):
        if(n%i==0):
            count+=1
    if (count==2):
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")
num(n=int(input("enter the number:")))

#Method 2
def num(n):
    if(n>1):
        count=0
        for i in range(2,n//2+1):
            if(n%i==0):
                count+=1
        if (count==0):
            print(f"{n} is a prime number.")
        else:   
            print(f"{n} is not a prime number.")
    else:
        print(f"{n} is not a prime number")
num(n=int(input("enter the number:")))
