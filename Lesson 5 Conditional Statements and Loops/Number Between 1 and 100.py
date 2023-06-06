# Read user input
number = float(input())
# Logic
while number < 1 or number > 100:
    number = float(input())
print(f"The number {number:.1f} is between 1 and 100")
# Output
