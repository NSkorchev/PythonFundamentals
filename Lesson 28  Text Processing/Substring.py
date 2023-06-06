# Read user input
first = input()
second = input()
# Logic
while first in second:
    second = second.replace(first, "")

# Output
print(second)