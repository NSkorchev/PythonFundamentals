# Read user input
n = int(input())
current_value = 0
highest_value = 0
snowball_weight = 0
snowball_time = 0
snowball_quality = 0
# Logic
for i in range(1, n + 1):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())

    current_value = (weight / time_needed) ** quality

    if current_value > highest_value:
        highest_value = current_value
        snowball_weight = weight
        snowball_time = time_needed
        snowball_quality = quality

# Output
print(f"{snowball_weight} : {snowball_time} = {highest_value:.0f} ({snowball_quality})")