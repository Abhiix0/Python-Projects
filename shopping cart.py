#shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter food item (or type 'done' to finish): ")
    if food.lower() == 'done':
        break
    else:
        price = float(input(f"Enter price for {food}: "))
        prices.append(price)
        foods.append(food)

print("\nShopping Cart Summary:")
for food in foods:
    print(food, end=' ')
print("\nTotal price of items in the cart:")
for price in prices:
    total += price
print(total)