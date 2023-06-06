# Read user input
people = list(map(int, input().split()))
k = int(input())

index = 0
executed_list = []
executed = 0


# Logic
while len(people) > 0:
    executed += 1

    if executed % k == 0:
        executed_list.append(people.pop(index))
    else:
        index += 1

    if index >= len(people):
        index = 0

# Output
print(str(executed_list).replace(' ', '').replace('\'', ''))