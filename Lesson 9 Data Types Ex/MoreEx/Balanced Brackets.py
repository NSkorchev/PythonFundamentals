# Read user input
n = int(input())
counter = 0

# Logic
for i in range(n):
    line = input()
    if counter == 2 or counter == -1:
        break
    if line == "(":
        counter += 1
    if line == ")":
        counter -= 1

# Output
if counter == 0:
    print("BALANCED")
else:
    print("UNBALANCED")