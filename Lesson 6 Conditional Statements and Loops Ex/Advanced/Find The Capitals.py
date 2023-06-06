# Read user input
word = input()
x = ''

# Logic
for i in range(0, len(word)):
    if word[i].isupper():
        x += str(i)
y = ', '.join(x)
# Output
print(f"[{y}]")



# commands = input()
# idx = []
#
# for i in range(len(commands)):
#     if commands[i].isupper():
#         idx.append(i)
#
# print(idx)