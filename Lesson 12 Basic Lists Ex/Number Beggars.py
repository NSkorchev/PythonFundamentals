# Read user input
numbers = input().split(", ")
count_beggars = int(input())

result = [0] * count_beggars

# Logic
for i in range(len(numbers)):
    beggar_idx = i % count_beggars
    num = int(numbers[i])
    result[beggar_idx] += num

# Output
print(result)
