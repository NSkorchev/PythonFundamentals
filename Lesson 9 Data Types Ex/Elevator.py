# Read user input
n = int(input())
p = int(input())
# Logic
courses = n // p
leftover = n % p

if leftover > 0:
    result = courses + 1
else:
    result = courses
# Output
print(result)
