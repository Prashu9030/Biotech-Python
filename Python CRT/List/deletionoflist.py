IPL_List=["CSK","RCB","MI","SRH","GT","PBKS"]
print(IPL_List)
print("After deletion")
del IPL_List[4]
print(IPL_List)

Front_End=['HTML','CSS','javascript','React js']
print(Front_End)
Front_End.append('Angular js')
Front_End.append('Expressn js')
Front_End.insert(3,'Bootstrap')
print(Front_End)
Front_End.insert(2,'tailwind')
print(Front_End)
Front_End.pop(0)
print(Front_End)
Front_End.remove('CSS')
print(Front_End)
print(Front_End.index('React js'))
print(Front_End.index('javascript'))

Num=[1,2,3,4,5,6,7,8,9,10]
print(Num)
Num.reverse()
print(Num)
Num1=[1,2,3,4,5,6,7,8,9,10]
print(Num1)
Num2=[11,12,13,14,15,16,17,18,19,20]
print(Num2)
Num1.extend(Num2)
print(Num1)
Num1.sort()
print(Num1)
Num1.sort(reverse=True)
print(Num1)
#EXAMPLE-PARTY CODE
Guest_list=[]
print("Welcome to party project")
while(True):
    print("1.Enter 1 to add a guest")
    print("2.Enter 2 to remove a guest who cancels")
    print("3.Enter 3 to check a friend is on the list or not")
    print("4.Enter 4 to sort and print the final guest list")
    print("5.Enter 5 to exit")
    choice=int(input("Enter your choice-"))
    if(choice>=1 and choice<=5):
        if(choice==1):
            Name=input("Enter the guest name:")
            Guest_list.append(Name)
            print(f"{Name} is added to the guest list")
        elif(choice==2):
            cancelled_name=input("Enter the name of the guest who cancelled")
            if cancelled_name in Guest_list:
                Guest_list.remove(cancelled_name)
                print(f"{cancelled_name} is Removed from Guest List")
            else:
                print(f"{cancelled_name} is not present in Guest List")
        elif(choice==3):
            check_guest=input("Enter the guest name")
            if check_guest in Guest_list:
                print(f"{check_guest} is attending the party")
            else:
                print(f"{check_guest} is not attending the party")
        elif(choice==4):
            Guest_list.sort()
            print("Here's the final list of guests")
            print(Guest_list)
    else:
        print("Enjoy the party")
    break
