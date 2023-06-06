# Read user input
factor = int(input())
count = int(input())
result = []
# Logic
for i in range(factor, count * factor + factor, factor):
    result.append(i)

# Output
print(result)