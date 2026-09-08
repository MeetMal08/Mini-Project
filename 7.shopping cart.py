# Python Shopping Cart Program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a Food to buy (or type 'done' to finish): ")
    if food == "done":
        break
    else:
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)

print("-----YOUR SHOPPING CART-----")
for food in foods:
    print(food, end=", ")

for i in range(len(foods)):
    total += prices[i]

print(f"Your total is: ${total:.2f}")


