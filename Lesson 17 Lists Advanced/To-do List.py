# Read user input
to_do_list = [0] * 10
command = input()
# Logic

while command != "End":
    importance, task = command.split("-")
    importance = int(importance)
    index = importance - 1
    to_do_list[index] = task
    command = input()

# Output
print([task for task in to_do_list if task != 0])