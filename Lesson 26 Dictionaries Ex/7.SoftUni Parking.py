license_plate_by_name = {}


count = int(input())

for idx in range(count):
    command_args = input().split()
    command = command_args[0]
    name = command_args[1]

    if command == "register":
        license_plate = command_args[2]
        if name in license_plate_by_name:
            print(f"ERROR: already registered with plate number {license_plate_by_name[name]}")
        else:
            license_plate_by_name[name] = license_plate
            print(f"{name} registered {license_plate} successfully")
    else:
        if name in license_plate_by_name:
            license_plate_by_name.pop(name)
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")

for name, license_plate in license_plate_by_name.items():
    print(f"{name} => {license_plate}")