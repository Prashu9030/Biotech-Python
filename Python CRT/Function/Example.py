employee={}
def print_emp():
    if bool(employee):
        print("Here's the list of employees...!")
        print(employee)
    else:
        print("list is empty")
def add_emp():
    name=input("enter the full name as per adhaar :")
    Id=input("enter the employee id :")
    doj=input("enter the date of joining in DD-MM-YYYY format :")
    job=input("enter your designation :")
    dept=input("enter yor department :")
    sal=float(input("enter you salary :"))
    promotion_status=input("enter 'YES' if serving period else 'NO' :")
    mode=input("enter the mode of assignment(WHF/WFO):")
    notice_period=input("enter 'YES' if serving period else 'NO' ")
    emp=[name,Id,doj,job,dept,sal,promotion_status,mode,notice_period]
    employee[Id]=emp
    print("employee added....!")
def Remove_Emp():
    ID=input("Enter the ID of the Employee :")
    del employee[ID]
    print("EMployee Removed...!")
def Verify_Background():
    ID=input("Enter the ID of Employee whom you have to verify :")
    Verify=input(f"Enter Yes if Background Verification is completed :")
    if Verify in "Yes yes":
        print("Verification is completed")
    else:
        print("Verification is Pending!!!!!!!!")
while True:
    print("Employee Management &Onboarding Process")
    print("1. enter 1 to print the Current Employee Details :")
    print("2. enter 2 to add a new employee Details :")
    print("3. enter 3 to Remove a Employee")
    print("4. enter 4 to Check the background Verification :")
    print("5. enter 5 to print the Final List/dict of the Employees")
    print("6. Exit")
    choice=int(input("enter your choice :"))
    if (choice>=1 and choice<=6):
        if(choice == 1):
            print_emp()
        elif choice==2:
            add_emp()
        elif choice==3:
            Remove_Emp()
        elif choice==4:
             Verify_Background()
        elif choice==5:
            print(list(employee))
        else:
            print("Danyavadamulu ")
            break
    else:
        print("Enter the Valid input")