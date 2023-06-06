# Read user input
number = int(input())
# Logic
if number > 1:
    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            print(False)
            break
    else:
        print(True)
else:
    print(False)
# Output
