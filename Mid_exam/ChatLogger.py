# Read user input
chat_history = []
# Logic
while True:

    line = input()
    if line == "end":
        break

    commands = line.split()

    command = commands[0]
    message = commands[1]

    if command == "Chat":
        chat_history.append(message)
    elif command == "Delete" and message in chat_history:
        chat_history.remove(message)
    elif command == "Edit" and message in chat_history:
        new_message = commands[2]
        idx = chat_history.index(message)
        chat_history[idx] = new_message
    elif command == "Pin" and message in chat_history:
        chat_history.append(chat_history.pop(chat_history.index(message)))
    elif command == "Spam":
        for text in commands[1:]:
            chat_history.append(text)

# Output
print("\n".join(chat_history))