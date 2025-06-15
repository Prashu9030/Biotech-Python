n=int(input("Enter the input:"))
ec=0
oc=0
while n>0:
    r=n%10
    if r%2==0:
        ec+=1
    else:
        oc+=1
    n=n//10
print(f"The number of even digits are:{ec}")
print(f"The number of odd digits are:{oc}")
