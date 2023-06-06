import re

text = input()
daily_kcal = 2000
matches = re.findall(r"([#|])([A-Za-z\s]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1", text)
total_calories = 0
products = []

for match in matches:
    product = match[1]
    expired = match[2]
    calories = int(match[3])

    products.append(f"Item: {product}, Best before: {expired}, Nutrition: {calories}")
    total_calories += calories

days = total_calories // daily_kcal

print(f"You have food to last you for: {days} days!")
print('\n'.join(products))

