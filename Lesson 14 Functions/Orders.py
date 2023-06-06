# Read user input
def calculate_total_amount(product, quantity):
    if product == "water":
        result = quantity * 1
    elif product == "coffee":
        result = quantity * 1.50
    elif product == "coke":
        result = quantity * 1.40
    elif product == "snacks":
        result = quantity * 2
    return result


# Logic
product_to_buy = input()
requested_quantity = int(input())
# Output
total_amount = calculate_total_amount(product_to_buy, requested_quantity)
print(f"{total_amount:.2f}")