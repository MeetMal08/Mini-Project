# Concessions Stand Program
# This program allows the user to input items and their prices, and then calculates the total cost of the items purchased.
# dictionary {key:value}

MENU = {
    "Popcorn": 5.00,
    "Hot Dog": 3.00,
    "Nachos": 4.00,
    "Soda": 2.00
}
cart = []
total = 0

print("Welcome to the Concessions Stand!")
print("------MENU-----")

for key, value in MENU.items():
    print(f"{key}: ${value:.2f}")
print("-----------------")

while True:
    food = input("select and item from the menu (or type 'done' to finish): ")
    if food == "done":
        break
    elif food in MENU:
        cart.append(food)
        total += MENU[food]
    else:
        print("Invalid item. Please select from the menu.")

print("-----YOUR ORDER-----")
for food in cart:
    total +=MENU.get(food)
    print(food, end=", ")

print(f"Total cost: ${total:.2f}")

