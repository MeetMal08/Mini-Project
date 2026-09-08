# Python Compound Interest Calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principal amount (greater than 0): "))
    if principle <= 0:
        print("Principal amount must be greater than 0.")

while rate <= 0:
    rate = float(input("Enter the interest rate (greater than 0): "))
    if rate <= 0:
        print("Interest rate must be greater than 0.")

while time <= 0:
    time = float(input("Enter the time (greater than 0): "))
    if time <= 0:
        print("Time must be greater than 0.")
    if principle <= 0:
        print("Principal amount must be greater than 0.")

total = principle * (1 + rate / 100) ** time
print(f"The total amount after {time} years is: ${total:.2f}")



