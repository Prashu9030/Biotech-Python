Guest_list=[]
print("Welcome to party project")
while(True):
    print("Menu")
    print("1.enter 1 to add a guest")
    print("2.enter 2 remove a guest who cancels")
    print("3.enter 3 to check if a frieind is on the list or not")
    print("4,enter 4 to sort and print the final guest list")
    print("5.enter 5 to exit")
    Choice=int(input("Enter the Choice :"))
    if(Choice>=1 and Choice<=5):
        if(Choice==1):
            Name=input("Enter the Guest Name :")
            Guest_list.append(Name)
            print(f"{Name} is added to the guest list")
        elif(Choice==2):
            Cancelled_Name=input("Enter the name off the Guest who cancelled")
            if Cancelled_Name in Guest_list:
                Guest_list.remove(Cancelled_Name)
                print(f"{Name} is removed fron the Guest list ")
            else:
                print(f"{Name} is not in the guest list")
        elif(Choice==3):
            Check_Guest=input("Enter the Guest Name :")
            if Check_Guest in Guest_list:
                print(f"{Check_Guest} is in the list")
            else:
                print(f"{Check_Guest} is not in the list")
        elif(Choice==4):
            Guest_list.sort()
            print("Here's is the Finalised List ")
            print(Guest_list)
    else:
        print("Enjoy the Party")
        break