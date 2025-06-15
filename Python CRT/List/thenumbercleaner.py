Size=int(input("Enter the Range of the List :"))
Num=[]
for i in range(Size):
    Temp=int(input(f"Enter the value at {i} Index:"))
    Num.append(Temp)
print(f"Original List :{Num}")
for i in range(Size):
    if(Num[i]<0):
        Num[i]=0
    if(Num[i]%3==0):
        print(f"Updated List :{Num}")