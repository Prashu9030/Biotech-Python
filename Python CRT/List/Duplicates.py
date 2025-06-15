Size=int(input("Enter the Size of List:"))
List=[]
Unique_List=[]
for i in range(Size):
    Temp=int(input(f"Enter the Integer Value at {i} Index Position:"))
    List.append(Temp)
print(f"User Enterd List:{List}")
for i in List:
    if i not in Unique_List:
        Unique_List.append(i)
print(f"Unique List:{Unique_List}")
