#Temperature converter  

temperature = float(input("Enter temperature:"))
unit = input("Enter unit (C/F): ").strip().lower()  
if unit == 'c':
    converted_temp = (temperature * 9/5) + 32
    print(f"{temperature}°C is equal to {converted_temp:.2f}°F")
elif unit == 'f':
    converted_temp = (temperature - 32) * 5/9
    print(f"{temperature}°F is equal to {converted_temp:.2f}°C")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
