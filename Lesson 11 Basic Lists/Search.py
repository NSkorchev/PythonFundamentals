# Read user input
n = int(input())
word = input()
all_strings = []
string_containing_word = []
# Logic
for i in range(0, n):
    command = input()
    all_strings.append(command)

    if word in command:
        string_containing_word.append(command)


# Output
print(all_strings)
print(string_containing_word)