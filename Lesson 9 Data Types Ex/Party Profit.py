# Read user input
group_size = int(input())
adventure_days = int(input())
coins = 0

# Logic
for i in range(1, adventure_days + 1):
    if i % 10 == 0:
        group_size -= 2

    if i % 15 == 0:
        group_size += 5
        coins -= 2 * group_size

    coins += 50
    coins -= 2 * group_size

    if i % 3 == 0:
        coins -= 3 * group_size
    if i % 5 == 0:
        coins += 20 * group_size

# Output
print(f"{group_size} companions received {coins // group_size} coins each.")
