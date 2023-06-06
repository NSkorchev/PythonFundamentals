# Read user input
hapiness = input().split(" ")
factor = int(input())

# Logic
hapiness = list(map(lambda x: int(x) * factor, hapiness))
filtered = list(filter(lambda x: x >= (sum(hapiness) / len(hapiness)), hapiness))

# Output
if len(filtered) >= len(hapiness) / 2:
    print(f"Score: {len(filtered)}/{len(hapiness)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(hapiness)}. Employees are not happy!")
