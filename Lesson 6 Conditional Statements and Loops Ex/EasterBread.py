# Read user input
budget = float(input())
flour_price = float(input())
eggs_price = 0.75 * flour_price
milk_price = 1.25 * flour_price / 4

colored_eggs_count = 0
bread_loaves = 0

easter_bread_price = eggs_price + milk_price + flour_price

# Logic
while easter_bread_price <= budget:
    budget -= easter_bread_price
    bread_loaves += 1
    colored_eggs_count += 3
    if bread_loaves % 3 == 0:
        colored_eggs_count -= (bread_loaves - 2)

    money_left = budget % (bread_loaves * easter_bread_price)

# Output
print(f"You made {bread_loaves} loaves of Easter bread! Now you have {colored_eggs_count} eggs and {budget:.2f}BGN left.")