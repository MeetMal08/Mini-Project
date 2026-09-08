# Python Weight Converter

weight = float(input("Enter your weight: "))
unit = input("Enter the unit (kg, lb): ")  

if unit == "kg": 
    converted_weight = weight * 2.20462
    print(f"{weight} kg is equal to {converted_weight:.2f} lb")
elif unit == "lb":
    converted_weight = weight / 2.20462
    print(f"{weight} lb is equal to {converted_weight:.2f} kg")
else:
    print("Invalid unit")