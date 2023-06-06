# Read user input
divisor = int(input())
boundary = int(input())

# Logic
for N in range(1, boundary + 1):
    if N % divisor == 0:
        result = N
# Output
print(result)