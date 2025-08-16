#banking prograam using functions
def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if amount > balance:
        return balance
    return balance - amount

def check_balance(balance):
    return balance

def main():
    balance = 1000
    while True:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            balance = deposit(balance, amount)
            print("Deposited:", amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            new_balance = withdraw(balance, amount)
            if new_balance == balance:
                print("Insufficient funds")
            else:
                balance = new_balance
                print("Withdrawn:", amount)
        elif choice == '3':
            print("Balance:", check_balance(balance))
        elif choice == '4':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()