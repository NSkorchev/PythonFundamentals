# Read user input
# Logic
empty = "0"
first = "1"
second = "2"
final = []
for i in range(0, 3):
    field = input().split()

    idx1 = field[0]
    idx2 = field[1]
    idx3 = field[2]
    final.append(idx1)
    final.append(idx2)
    final.append(idx3)

    if final[0] == final[1]


# Output
print(final)