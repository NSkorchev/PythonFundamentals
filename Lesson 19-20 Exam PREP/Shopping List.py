initial_list = input().split("!")

while True:
    line = input()
    if line == "Go Shopping!":
        break

    commands = line.split()
    command_arg = commands[0]
    product = commands[1]

    if command_arg == "Urgent" and product not in initial_list:
        initial_list.insert(0, product)
    elif command_arg == "Unnecessary" and product in initial_list:
        initial_list.remove(product)
    elif command_arg == "Correct" and product in initial_list:
        product_new = commands[2]
        idx = initial_list.index(product)
        initial_list[idx] = product_new
    elif command_arg == "Rearrange" and product in initial_list:
        initial_list.remove(product)
        initial_list.append(product)

print(", ".join(initial_list))
