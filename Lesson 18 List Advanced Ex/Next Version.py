# Read user input
major, minor, patch = [int(x) for x in input().split(".")]
# Logic
patch += 1
if patch == 10:
    patch = 0
    minor += 1

    if minor == 10:
        minor = 0
        major += 1
# Output
print(f"{major}.{minor}.{patch}")
