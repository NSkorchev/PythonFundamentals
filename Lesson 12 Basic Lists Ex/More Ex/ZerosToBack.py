# Read user input
numbers = [int(x) for x in input().split(", ")]
counter = 0
# Logic
num_zeros = numbers.count(0)

numbers = [x for x in numbers if x != 0]
numbers.extend([0] * num_zeros)
# Output
print(numbers)