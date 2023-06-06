# Read user input
items = input().split("|")
budget = float(input())

profit = []
total_profit = 0

# Logic
for item in items:
    item_type, Max_price = (item.split("->"))
    Max_price = float(Max_price)
    # print(type)
    # print(Max_price)
    if item_type == "Clothes" and Max_price > 50.00:
        continue
    if item_type == "Shoes" and Max_price > 35.00:
        continue
    if item_type == "Accessories" and Max_price > 20.5:
        continue

    if budget >= Max_price:
        budget -= Max_price
        profit.append(Max_price * 1.4)
        total_profit += Max_price * 0.4
        # print(profit)

# Output
for i in profit:
    print(f"{i:.2f}", end=" ")
print(f"\nProfit: {total_profit:.2f}")
if sum(profit) + budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")