# Read user input
n = int(input())
start = 97
# Logic
for first in range(start, start + n):
    for second in range(start, start + n):
        for third in range(start, start + n):
            print(f"{chr(first)}{chr(second)}{chr(third)}")
# Output
