# Read user input


def characters(start, end):
    result = []
    for i in range(ord(start) + 1, ord(end)):
        result.append(chr(i))
    return result


start_char = input()
end_char = input()


# Logic
# Output
ch_in_range = characters(start_char, end_char)
print(" ".join(ch_in_range))
