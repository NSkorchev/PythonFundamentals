# Read user input
words = input().split()
char_count = {}
# Logic
for word in words:
    for letter in word:
        if letter in char_count:
            char_count[letter] += 1
        else:
            char_count[letter] = 1
# Output
for key, value in char_count.items():
    print(f'{key} -> {value}')
