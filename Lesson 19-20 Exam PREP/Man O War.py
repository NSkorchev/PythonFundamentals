# Read user input
def is_valid_idx(idx, seq):
    return 0 <= idx < len(seq)


pirate_ship = [int(x) for x in input().split(">")]
warship_status = [int(x) for x in input().split(">")]
max_health = int(input())

# Logic
is_running = True
while is_running:
    line = input()
    if line == "Retire":
        break

    command_arg = line.split()
    command = command_arg[0]

    if command == "Fire":
        idx = int(command_arg[1])
        damage = int(command_arg[2])
        if not is_valid_idx(idx, warship_status):
            continue
        warship_status[idx] -= damage
        if warship_status[idx] <= 0:
            is_running = False
            print("You won! The enemy ship has sunken.")


    elif command == "Defend":
        start_idx = int(command_arg[1])
        end_idx = int(command_arg[2])
        damage = int(command_arg[3])
        if not is_valid_idx(start_idx, pirate_ship) or not is_valid_idx(end_idx, pirate_ship):
            continue
        for idx in range(start_idx, end_idx + 1):
            pirate_ship[idx] -= damage
            if pirate_ship[idx] <= 0:
                is_running = False
                print("You lost! The pirate ship has sunken.")
                break

    elif command == "Repair":
        idx = int(command_arg[1])
        health = int(command_arg[2])
        if not is_valid_idx(idx, pirate_ship):
            continue
        pirate_ship[idx] = min(max_health, pirate_ship[idx] + health)

    elif command == "Status":
        threshold = max_health * 0.2
        counter = 0
        for section in pirate_ship:
            if section < threshold:
                counter += 1
        print(f"{counter} sections need repair.")

# Output
if is_running:
    print(f"Pirate ship status: {sum(pirate_ship)}\nWarship status: {sum(warship_status)}")
