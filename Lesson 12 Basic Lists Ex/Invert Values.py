# Read user input
numbers = input().split()
result = []
# Logic
for i in numbers:
    number = int(i)
    result.append(-number)
# Output
print(result)