Size=int(input("Enter the range of List:"))
Num=[]
Temp=0
for i in range(Size):
    Value=int(input(f"enter the value at {i} Index:"))
    Num.append(Value)
print(f"Orgianl List:{Num}")
for i in range(Size):
    if (Num[i]<0):
        Num[i]=0
    if(Num[i]%3==0):
        print(Num[i])
