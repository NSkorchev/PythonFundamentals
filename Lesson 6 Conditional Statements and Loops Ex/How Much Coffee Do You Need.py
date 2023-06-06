# Read user input
coffee = 0
command = ''
# Logic
while command != 'END':
    command = input()

    lower_case_word = command.lower()
    if lower_case_word == 'dog' or lower_case_word == 'cat' or lower_case_word == 'coding' or lower_case_word == 'movie':
        if command.isupper():
            coffee += 2
        else:
            coffee += 1
    # if commands == 'dog' or commands == 'cat' or commands == 'coding' or commands == 'movie':
    #     coffee += 1
    # elif commands == 'DOG' or commands == 'CAT' or commands == 'CODING' or commands == 'MOVIE':
    #     coffee += 2
    # else:
    #     continue

# Output
if coffee > 5:
    print("You need extra sleep")
else:
    print(f'{coffee}')
