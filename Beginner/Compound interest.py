#compound interest calculator
print("Welcome to the Compound Interest Calculator!")
while True:
    try:
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the annual interest rate (in %): "))
        times = int(input("Enter the number of times interest is compounded per year: "))
        years = float(input("Enter the number of years: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue

    amount = principal * (1 + rate / 100 / times) ** (times * years)
    print(f"After {years} years, the amount will be: {amount:.2f}")

    again = input("Do you want to calculate again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thank you for using the Compound Interest Calculator!")
        break

 



