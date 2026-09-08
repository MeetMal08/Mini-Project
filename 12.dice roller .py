# Python Dice Roller 

import random

print("Welcome to the Dice Roller!")

#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518 ")

#● ┌ ─ ┐ │ └ ┘

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"
dice_art = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"
    )
}

dice = []
total = 0
num_of_dice = int(input("How many dice would you like to roll?: "))

for i in range(num_of_dice):
    roll = random.randint(1, 6)
    dice.append(roll)
    total += roll

print("You rolled:")
for roll in dice:
    for line in dice_art[roll]:
        print(line)
print(f"Total: {total}")