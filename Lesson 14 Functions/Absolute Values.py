# Read user input
numbers = input().split()
result = []
# Logic
def absolute_values():
    for i in numbers:
        number = float(i)
        result.append(abs(number))
    print(result)

# Output
absolute_values()