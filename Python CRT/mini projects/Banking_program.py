def show_balance(balance):
    print(f"Your balance is {balance:.2f} rupees")

def deposit():
    amount = float(input("Enter an amount to be deposited: "))
    if amount < 0:
        print("That's not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn: "))
    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount
    
balance = 0
while True:
    print("   Banking Program   ")
    print("1. Enter 1 to Show Balance")
    print("2. Enter 2 toDeposit")
    print("3. Enter 3 to Withdraw")
    print("4. Enter 4 to Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        show_balance(balance)
    elif choice == '2':
        balance += deposit()
    elif choice == '3':
        balance -= withdraw(balance)
    elif choice == '4':
        break
    else:
        print("That is not a valid choice")
print("Thank you! Have a nice day!")
