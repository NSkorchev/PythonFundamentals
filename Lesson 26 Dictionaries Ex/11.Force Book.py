command = input()

unique_users_side = {}
unique_side_users = {}

while command != "Lumpawaroo":

    if " | " in command:
        force_side, force_user = command.split(" | ")

        if force_side not in unique_users_side:
            unique_users_side[force_side] = []

        if force_user not in unique_side_users:
            unique_side_users[force_user] = force_side
            unique_users_side[force_side].append(force_user)

    else:
        force_user, force_side = command.split(" -> ")

        if force_side not in unique_users_side:
            unique_users_side[force_side] = []

        unique_users_side[force_side].append(force_user)

        if force_user in unique_side_users:
            old_side = unique_side_users[force_user]
            unique_users_side[old_side].remove(force_user)
            unique_side_users[force_user] = force_side
        else:
            unique_side_users[force_user] = force_side

        print(f"{force_user} joins the {force_side} side!")
    command = input()


for side, members in unique_users_side.items():
    if len(members) == 0:
        continue

    print(f"Side: {side}, Members: {len(members)}")
    for member in members:
        print(f"! {member}")

