# Read user input


def min_number():
    return f"The minimum number is {min(numbers)}"


def max_number():
    return f"The maximum number is {max(numbers)}"


def sum_numbers():
    return f"The sum number is: {sum(numbers)}"


numbers = list(map(int, input().split(" ")))
# Logic
# Output
print(f"{min_number()}\n{max_number()}\n{sum_numbers()}")
