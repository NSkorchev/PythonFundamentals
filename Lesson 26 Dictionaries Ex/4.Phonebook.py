phonebook = {}

n = 0
while True:
    line = input()
    parts = line.split("-")
    if len(parts) == 1:
        n = int(line)
        break

    name = parts[0]
    phone = parts[1]

    phonebook[name] = phone

for i in range(n):
    find_name = input()
    if find_name in phonebook.keys():
        print(f"{find_name} -> {phonebook[find_name]}")
    else:
        print(f"Contact {find_name} does not exist.")
