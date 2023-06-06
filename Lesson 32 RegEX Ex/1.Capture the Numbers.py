import re
# Read user input
result = []
pattern = r"\d+"

# Logic
while True:
    line = input()
    if not line:
        break

    digits = re.findall(pattern, line)
    result.extend(digits)

# Output
print(' '.join(result))
