# Read user input
numbers = list(map(int, input().split(" ")))
# numbers = [int(x) for x in input().split(" ")]
# Logic


def even_numbers(num):
    return num % 2 == 0


# Output
print(list(filter(even_numbers, numbers)))