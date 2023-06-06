# Read user input
sequence = input().split()
text = input()

message = ""
index = 0
# Logic
for num in sequence:
    index += sum(int(digit) for digit in num)
    if index > len(text):
        index -= len(text)

    # print(idx)
    message += text[index]
    text = text[:index] + text[index + 1:]
    # print(action)
    index = 0

print(message)
