# calculator.py
# Simple Calculator Program
print("Welcome to the Simple Calculator!")
op = input("Enter operator (+, -, *, /): ")
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))

if op == '+':
    result = n1 + n2    
    print(f"The result of {n1} + {n2} is: {result}")
elif op == '-':     
    result = n1 - n2    
    print(f"The result of {n1} - {n2} is: {result}")
elif op == '*':
    result = n1 * n2    
    print(f"The result of {n1} * {n2} is: {result}")
elif op == '/':
    if n2 != 0:
        result = n1 / n2    
        print(f"The result of {n1} / {n2} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid operator. Please use +, -, *, or /.")

