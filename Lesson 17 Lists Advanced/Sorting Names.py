# Read user input
names = input().split(", ")

# Logic
sorted_names = sorted(names, key=lambda x: (-len(x), x))
# Output
print(sorted_names)