# Python Credit Card Validation Program

#1. Remove any '-' or ' '
#2.Add all digits in the odd places from right to left
#3. double every second digit from right to left.
#       (If result is a two digit number, add the digits to get a single digit number)
# 4. Sum the totals of steps 2 , 3
# 5. If sum is divisible by 10 , the credit card number is valid, else invalid. 

sum_odd_digits = 0
sum_even_digits = 0
total_sum = 0

# Step 1: Get the credit card number from the user
credit_card_number = input("Enter the credit card number: ")
credit_card_number = credit_card_number.replace("-", "") # Remove dashes if any
credit_card_number = credit_card_number.replace(" ", "")  # Remove spaces if any
credit_card_number = credit_card_number[::-1]  # Reverse the credit card number for easier processing
print(f"Credit Card Number: {credit_card_number}")

# Step 2: Add all digits in the odd places from right to left
for x in credit_card_number[::2]:  # Get every second digit starting from the right (odd places)
    sum_odd_digits += int(x)

# Step 3: Double every second digit from right to left and sum the digits if necessary
for x in credit_card_number[1::2]:  # Get every second digit starting from the right (even places)
    x = int(x) * 2
    if x > 10:  # If the result is a two-digit number, add the digits together
        sum_even_digits += (x // 10) + (x % 10)
    else:
        sum_even_digits += x

# Step 4: Sum the totals of steps 2 and 3
total_sum = sum_odd_digits + sum_even_digits

# Step 5: Check if the total is divisible by 10
if total_sum % 10 == 0:
    print("The credit card number is valid.")
else:
    print("The credit card number is invalid.")

