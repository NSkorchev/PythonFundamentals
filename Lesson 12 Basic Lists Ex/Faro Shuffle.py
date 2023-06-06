# Read user input
cards = input().split()
faro_shuffles = int(input())

# Logic
for i in range(faro_shuffles):
    half = int(len(cards) / 2)
    result1 = cards[:half]
    result2 = cards[half:]
    result = []

    for j in range(half):
        result.append(result1[j])
        result.append(result2[j])
    cards = result

# Output
print(cards)
