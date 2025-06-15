n=int(input("Enter the input:"))
for i in range(1,n+1):
    print(f"Multiplication table of {i}")
    for j in range(1,11):
        print(f"{i} x {j} = {i * j}")
#Reverse multiplication
n=int(input("Enter the input:"))
for i in range(1,n+1):
    print(f"Multiplication table of {i}")
    for j in range(10,0,-1):
        print(f"{i} x {j} = {i * j}")
