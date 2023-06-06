# Read user input
def is_palindrome():
    for num in numbers:
      is_valid = num == "".join(reversed(num))
      print(is_valid)
    return


numbers = input().split(", ")
# Logic
# Output
is_palindrome()
