# Read user input
text_wrap = input()

def remove_vowels():
    # removed_sum = []
    # for char in text_wrap:
    #     if char.lower() not in ['a', 'o', 'u', 'e', 'i']:
    #         removed_sum.append(char)
    result = [char for char in text_wrap if char.lower() not in ['a', 'o', 'u', 'e', 'i']]
    result = "".join(result)
    return result
# Logic
print(remove_vowels())
# Output
