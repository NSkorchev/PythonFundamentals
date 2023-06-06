# Read user input
quantity_decorations = int(input())
days_left = int(input())
christmas_spirit = 0
budget = 0

ornament_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

ornament_set = 5
tree_skirt = 3
tree_garland = 10
tree_lights = 17
# Logic

for i in range(1, days_left + 1):
    if i % 11 == 0:
        quantity_decorations += 2
    if i % 2 == 0:
        christmas_spirit += 5
        budget += quantity_decorations * ornament_price
    if i % 3 == 0:
        christmas_spirit += 13
        budget += quantity_decorations * (tree_skirt_price + tree_garland_price)
    if i % 5 == 0:
        christmas_spirit += 17
        budget += tree_lights_price * quantity_decorations
        if i % 3 == 0:
            christmas_spirit += 30
    if i % 10 == 0:
        christmas_spirit -= 20
        budget += tree_skirt_price + tree_garland_price + tree_lights_price
if days_left % 10 == 0:
    christmas_spirit -= 30

# Output
print(f"Total cost: {budget}")
print(f"Total spirit: {christmas_spirit}")
