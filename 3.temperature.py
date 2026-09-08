#Python Temperature Converter

unit = input("Enter the unit you want to convert from (C for Celsius, F for Fahrenheit): ")

temperature = float(input("Enter the temperature: "))

if unit == "C":
    converted_temperature = (temperature * 9/5) + 32
    print(f"{temperature}°C is equal to {converted_temperature:.2f}°F")

elif unit == "F":
    converted_temperature = (temperature - 32) * 5/9
    print(f"{temperature}°F is equal to {converted_temperature:.2f}°C")

else:
    print("Invalid unit")  