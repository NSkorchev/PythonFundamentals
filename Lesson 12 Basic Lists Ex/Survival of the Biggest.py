# Read user input
numbers = input().split()
numbers = [int(x) for x in numbers]
n = int(input())

# Logic
for i in range(n):
    min_number = min(numbers)
    numbers.remove(min_number)

result = ""
for i in range(0, len(numbers)):
    result += str(numbers[i])
    if i != len(numbers) - 1:
        result += ", "

# Output
print(result)