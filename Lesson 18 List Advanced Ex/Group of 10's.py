from math import ceil
# Read user input
seq_of_numbers = list(map(int, input().split(", ")))

initial_low = 1
initial_high = 10

max_num = ceil(max(seq_of_numbers) / 10)

for idx in range(1, max_num + 1):
    grouped_numbers = [x for x in seq_of_numbers if initial_low <= x <= initial_high]
    print(f"Group of {10 * idx}'s: {grouped_numbers}")

    initial_low += 10
    initial_high += 10



# Output
