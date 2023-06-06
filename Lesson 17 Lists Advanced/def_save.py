# lambda
def put_static():
    lambda x: x*10 if x<2 else (x**2 if x<4 else x+10)
# Logic

# map is a function that takes two or more arguments: a function and an iterable (such as a list, tuple, or array).
# The function is applied to each element of the iterable and a new iterable is returned,
# containing the results of the function applied to each element. Here's a simple example:
def square(num):
  return num**2

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)

# filter is a function that takes two arguments: a function and an iterable.
# The function is applied to each element of the iterable and a new iterable is returned,
# containing only the elements for which the function returns True. Here's an example:

def is_even(num):
  return num % 2 == 0

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)

# new_list = [expression for item in iterable if condition]
# Where expression is the operation to be performed on each element in the iterable,
# item is the variable to hold each element of the iterable,
# and condition is an optional filter that allows you to select only certain elements based on a condition.
# List comprehensions are often more readable and concise than using map and filter functions,
# and they can also be faster than using map and filter for simple transformations.