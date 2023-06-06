# Read user input
initial_energy = 100
initial_coins = 100

events = input().split("|")
bankrupcy = False
# Logic
for event in events:
    # print(event)
    command, number = event.split("-")
    number = int(number)
    # print(ingredient)
    # print(energy)

    if command == "rest":
        gained_energy = min(100 - initial_energy, number)
        initial_energy += gained_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {initial_energy}.")
        # if initial_energy + lesson <= 100:
        #     initial_energy += lesson
        #     print(f"You gained {lesson} energy.")
        #     print(f"Current energy: {initial_energy}.")
        # else:
        #     print(f"You gained 0 energy.")
        #     print(f"Current energy: {initial_energy}.")

    elif command == "order":
        if initial_energy - 30 >= 0:
            initial_energy -= 30
            initial_coins += number
            print(f"You earned {number} coins.")
        else:
            initial_energy += 50
            print("You had to rest!")

    else:
        if initial_coins - number >= 0:
            initial_coins -= number
            print(f"You bought {command}.")
        else:
            print(f"Closed! Cannot afford {command}.")
            bankrupcy = True
            break

# Output
if bankrupcy == False:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")