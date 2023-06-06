# Read user input
capacity = 255
n = int(input())
volume = 0
# Logic
for i in range(n):
    liters = int(input())

    if liters >= capacity:
        print("Insufficient capacity!")
    else:
        capacity -= liters
        volume += liters

# Output
print(f"{volume}")