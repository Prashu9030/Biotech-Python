#EXAMPLE-SANTA CODE
Toys_list=[]
unique_list=[]
print("Welcome to Santa's Sleigh Packing")
while(True):
    print("1.Enter 1 to enter the toy name")
    print("2.Enter 2 to view the toys list")
    print("3.Enter 3 to Remove the duplicates")
    print("4.Enter 4 to sort and print the final list")
    choice=int(input("Enter your choice:"))
    if(choice>=1 and choice<=4):
        if(choice==1):
            name=input("Enter the toy name")
            Toys_list.append(name)
            print(f"{name} is added to the list")
        elif(choice==2):
            print("The list of the toys")
            print(Toys_list)
        elif(choice==3):
            for i in Toys_list:
                if i not in unique_list:
                    unique_list.append(i)
            print(f"unique list:{unique_list}")
        elif(choice==4):
            unique_list.sort()
            print("Here the final list of toys")
            print(unique_list)
    else:
        print("Santa Packing")
        break
