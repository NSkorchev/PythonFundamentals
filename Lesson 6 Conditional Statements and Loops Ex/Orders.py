# Read user input
n = int(input())
total_price = 0
# Logic
for orders in range(n):

    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= capsules_per_day <= 2000:
        order_price = days * price_per_capsule * capsules_per_day
        total_price += order_price
        print(f"The price for the coffee is: ${order_price:.2f}")

# Output
print(f"Total: ${total_price:.2f}")
