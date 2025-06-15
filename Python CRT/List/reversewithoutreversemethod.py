Size=int(input("enter Size of the List:"))
List=[]
for i in range(Size):
    Temp=int(input(f"Enter the integer value at index {i}:"))
    List.append(Temp)
print("user enterd List")

List=[10,20,30,40,50,60,70,80]
print(List)
print(List[::])
print(List[1:4:1])
print(List[::2])
print(List[::-1])

