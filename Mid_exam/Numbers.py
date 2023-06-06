# Read user input
def collapse(lst, num):
    return [i for i in lst if i >= num]

num_sequence = list(map(int, input().split(" ")))

# Logic
while True:
    line = input()
    if line == "Finish":
        break

    commands = line.split()

    text = commands[0]
    number = commands[1]
    number = int(number)

    if text == "Add":
        num_sequence.append(number)
    elif text == "Remove" and number in num_sequence:
        num_sequence.remove(number)
    elif text == "Replace" and number in num_sequence:
        new_number = commands[2]
        new_number = int(new_number)
        idx = num_sequence.index(number)
        num_sequence[idx] = new_number
    elif text == "Collapse":
        num_sequence = collapse(num_sequence, int(number))

# Output
result = list(map(str, num_sequence))
print(" ".join(result))
