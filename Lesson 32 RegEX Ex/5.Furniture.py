import re
# Read user input
pattern = r"^(?P<Furniture>>>[A-Za-z]+<<)(?P<Price>[\d]+.[\d]*)!(?P<Quantity>[\d]+)$"
regex_pattern = re.compile(pattern)


furnitures = []
total_price = 0

while True:
    line = input()

    if line == "Purchase":
        break

    match = re.findall(pattern, line)
    if match:
        groups = match[0]
        item = groups[0].strip('>><<')
        price = float(groups[1])
        quantity = int(groups[2])

        furnitures.append(item)
        total_price += price * quantity

print(f"Bought furniture:")

if len(furnitures) > 0:
    print('\n'.join(furnitures))

print(f"Total money spend: {total_price:.2f}")

#     purchases = re.finditer(regex_pattern, line)
#     for purchase in purchases:
#         purchase_data = purchase.groupdict()
#         furnitures.append((purchase_data['Furniture']).strip('>><<'))
#         total_price.append(float(purchase_data['Price']) * int(purchase_data['Quantity']))
#
#     line = input()
# print(f"Bought furniture:")
# for furniture in furnitures:
#     print(f"{furniture}")
# print(f"Total money spend: {sum(total_price)}")
