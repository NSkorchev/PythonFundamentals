# Read user input
gifts = input().split()
command = ""
# Logic
while True:
    command = input()
    if command == "No Money":
        break
    command_args = command.split()

    if command_args[0] == "OutOfStock":
        for i in range(len(gifts)):
            if gifts[i] == command_args[1]:
                gifts[i] = "None"
    elif command_args[0] == "Required":
        index = int(command_args[2])
        if index >= 0 and index < len(gifts):
            gifts[index] = command_args[1]
    elif command_args[0] == "JustInCase":
        gifts[-1] = command_args[1]

# Output
print(" ".join([gift for gift in gifts if gift != "None"]))