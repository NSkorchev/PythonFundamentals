# Read user input
n = int(input())
total_sum = 0
# Logic
for i in range(0, n):
    char = input()
    total_sum += ord(char)
# Output
print(f"The sum equals: {total_sum}")