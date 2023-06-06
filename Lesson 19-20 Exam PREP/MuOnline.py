# Read user input
health = 100
initial_bitcoins = 0
room_counter = 0
rooms = input().split("|")
dead = False
# Logic
for room in rooms:
    room_counter += 1
    command, number = room.split()
    number = int(number)

    if command == "potion":
        health += number
        if health >= 100:
            number = 100 - (health - number)
            health = 100
        print(f"You healed for {number} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        initial_bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            dead = True
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_counter}")
            break

# Output
if not dead:
    print(f"You've made it!\nBitcoins: {initial_bitcoins}\nHealth: {health}")

