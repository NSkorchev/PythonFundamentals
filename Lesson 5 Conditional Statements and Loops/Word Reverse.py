# Read user input
word = input()
print(word[::-1])
reversed_word = ''
# Logic
for i in range(len(word) - 1, -1, -1):
    # print(word[i], end='')
    reversed_word += word[i]

# Output
print(reversed_word)