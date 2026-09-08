#Python Banking Program
#1. Show Balance
#2. Deposit
#3. Withdraw

def show_balance():
    print("***************")
    print(f"Your balance is: ${balance:.2f}") # .2f formats the balance to 2 decimal places
    print("***************")


def deposit():
    print("***************")
    global balance
    amount = float(input("Enter amount to deposit: "))
    print("***************")

    if amount > 0:
        balance += amount
        print(f"Deposited ${amount:.2f}")
    else:
        print("Invalid amount. Please enter a positive number.")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if 0 < amount <= balance:
        balance -= amount
        print(f"Withdrew ${amount:.2f}")
    else:
        print("Invalid amount or insufficient funds.")

balance = 0
is_running = True

while is_running:
    print("Welcome to the Banking Program")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        show_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        is_running = False
    else:
        print("Invalid choice. Please try again.")

print("Thank you for using the Banking Program. Goodbye!")