# Read user input
data = input()
cities = {}

while data != "Sail":
    splitted_data = data.split("||")
    town = splitted_data[0]
    people = int(splitted_data[1])
    golds = int(splitted_data[2])

    if town not in cities:
        cities[town] = {"population": people, "gold": golds}
    else:
        cities[town]["population"] += people
        cities[town]["gold"] += golds

    data = input()

data = input()

while data != "End":
    splitted_data = data.split("=>")
    command = splitted_data[0]
    town = splitted_data[1]

    if command == "Plunder":
        people = int(splitted_data[2])
        golds = int(splitted_data[3])

        cities[town]["population"] -= people
        cities[town]["gold"] -= golds
        print(f"{town} plundered! {golds} gold stolen, {people} citizens killed.")

        if cities[town]["population"] <= 0 or cities[town]["gold"] <= 0:
            del cities[town]
            print(f"{town} has been wiped off the map!")

    elif command == "Prosper":
        golds = int(splitted_data[2])
        if golds >= 0:
            cities[town]["gold"] += golds
            print(f"{golds} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")
        else:
            print("Gold added cannot be a negative number!")

    data = input()
# Output
if not cities:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for town in cities:
        print(f"{town} -> Population: {cities[town]['population']} citizens, Gold: {cities[town]['gold']} kg")

