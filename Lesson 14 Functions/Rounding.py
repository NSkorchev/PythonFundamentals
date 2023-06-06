# Write a program that rounds all the given numbers, separated by a single space, and prints the removed_sum as a list. Use round().
# Read user input
numbers = input().split(" ")
# Logic


def round_numbers():
    result = []
    for number in numbers:

        number = float(number)
        number = round(number)
        result.append(number)

    return (result)


# Output
print(round_numbers())
