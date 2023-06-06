# Read user input


def is_substr(word, seq):
    for el in seq:
        found_substr = word in el
        if found_substr:
            return True
    return False


list_one = input().split(", ")
list_two = input().split(", ")

# Logic
result = [x for x in list_one if is_substr(x, list_two)]
# Output
print(result)
