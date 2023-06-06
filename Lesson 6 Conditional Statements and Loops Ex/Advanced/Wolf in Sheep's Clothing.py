# Read user input
animals = input()
lst = animals.split(", ")
n = len(lst)

# Logic
for i in range(n):

    if lst[n-1] == "wolf":
        print("Please go away and stop eating my sheep")
        break
    elif lst[i] == "wolf":
        print(f"Oi! Sheep number {n - i - 1}! You are about to be eaten by a wolf!" )

# Output
