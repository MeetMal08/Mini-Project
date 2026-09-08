# Python Slot Machine Program

from random import random


def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]

    return[random.choice(symbols) for _ in range(5)]

def print_row(row):
    print(" |".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
       if row[0] == "🍒":
            return bet * 3
    elif row[0] == "🍉":
            return bet * 4
    elif row[0] == "🍋":
            return bet * 5
    elif row[0] == "🔔":
            return bet * 10
    elif row[0] == "⭐":
            return bet * 20
    return 0

def main():
    balance = 100
    print("****************************")
    print("Welcome to the Slot Machine!")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")

    while balance > 0:
        print(f"Your current balance is: ${balance}")
        bet = float(input("Enter your bet amount (or 0 to quit): "))

        if bet == 0:
            print("Thank you for playing! Goodbye!")
            break
        elif bet > balance:
            print("You cannot bet more than your current balance.")
            continue
        
        # Spin the slot machine
        row1 = spin_row()
        row2 = spin_row()
        row3 = spin_row()
        
        print_row(row1)
        print_row(row2)
        print_row(row3)
        
        payout = get_payout(row1, bet)
        
        if payout > 0:
            print(f"Congratulations! You won ${payout}!")
            balance += payout
        else:
            print("Sorry, you didn't win this time.")
            balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row) 

        payout = get_payout(row, bet)  

        if payout > 0:
            print(f"Congratulations! You won ${payout}!")
            balance += payout
        else:
            print("Sorry, you didn't win this time.")
            balance -= bet

if __name__ == "__main__":
    main()

