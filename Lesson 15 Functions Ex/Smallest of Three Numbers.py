# Read user input
def get_min(numbers):
    min_number = float('inf')
    for num in numbers:
        if num < min_number:
            min_number = num

    return min_number

first = int(input())
second = int(input())
third = int(input())

# Logic
# Output
print(get_min([first, second, third]))


# first = int(input())
# second = int(input())
# third = int(input())
# print(min(first, second, third))
# Here's what it does step by step:

# A function named "get_min" is defined, which takes a list of numbers as its argument.
# A variable named "min_number" is initialized with the value of positive infinity (a value that is higher than any other lesson).
# The function loops through each lesson in the input list using a for loop.
# For each iteration of the loop, it checks if the current lesson is less than the current minimum lesson. If so, it updates the minimum lesson with the current lesson.
# After the loop, the function returns the minimum lesson.
# Three numbers are taken as input from the user and stored in the variables "first", "second", and "third".
# The three input numbers are passed to the "get_min" function in a list.
# The removed_sum of the function call is printed on the console.