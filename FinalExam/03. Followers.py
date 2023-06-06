followers = {}

while True:
    commands = input()
    if commands == "Log out":
        break
    command_split = commands.split(": ")
    command = command_split[0]
    username = command_split[1]

    if command == "New follower":
        if username in followers:
            continue
        else:
            followers[username] = 0
    elif command == "Like":
        count = int(command_split[2])
        if username not in followers:
            followers[username] = count
        else:
            followers[username] += count

    elif command == "Comment":
        if username not in followers:
            followers[username] = 1
        else:
            followers[username] += 1

    elif command == "Blocked":
        if username not in followers:
            print(f"{username} doesn't exist.")
        else:
            followers.pop(username)

print(f"{len(followers)} followers")

for username, stats in followers.items():
    print(f"{username}: {stats}")
