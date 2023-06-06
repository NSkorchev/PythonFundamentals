# Read user input
wagons = int(input())
trains = [0] * wagons
commands = input()

# Logic
while commands != "End":
    command = commands.split()[0]
    if command == "add":
        n_people = int(commands.split()[1])
        trains[-1] += n_people
    elif command == "insert":
        index = int(commands.split()[1])
        n_people = int(commands.split()[2])
        trains[index] += n_people
    elif command == "leave":
        index = int(commands.split()[1])
        n_people = int(commands.split()[2])
        trains[index] -= n_people

    commands = input()
# Output
print(trains)
