command = input()
products = {}

while command != "statistics":
    key, value = command.split(": ")
    value = int(value)

    if key not in products:
        products[key] = value
    else:
        products[key] += value

    command = input()

print("Products in stock:")
for key, value in products.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")