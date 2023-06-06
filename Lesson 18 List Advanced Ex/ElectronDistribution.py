# Read user input
num_electrons = int(input())
result = []

# Logic
while num_electrons > 0:
    n = len(result) + 1
    shell_value = min(2 * (n ** 2), num_electrons)
    result.append(shell_value)
    num_electrons -= shell_value

# Output
print(result)