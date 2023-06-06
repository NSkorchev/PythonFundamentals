# Read user input
lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
broken_shield = 0

expenses = 0
# Logic
for i in range(1, lost_fights + 1):
    broken_helmet = False
    broken_sword = False
    if i % 2 == 0:
        expenses += helmet_price
        broken_helmet = True
    if i % 3 == 0:
        expenses += sword_price
        broken_sword = True
    if broken_helmet and broken_sword:
        expenses += shield_price
        broken_shield += 1
    if broken_shield == 2:
        expenses += armor_price
        broken_shield = 0

# Output
print(f"Gladiator expenses: {expenses:.2f} aureus")