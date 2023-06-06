# Read user input
numbers = list(map(int, input().split(" ")))
# Logic


def sorted_nums():
    result = sorted(numbers, reverse=False)
    return result


# Output
print(sorted_nums())
