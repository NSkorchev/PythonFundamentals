# Read user input
number = float(input())

# Logic
if number == 0:
    print("zero")
elif number < 0:
    if -1 < number:
        print("small negative")
    elif number < -1000000:
        print("large negative")
    else:
        print("negative")
else:
    if 1 > number:
        print("small positive")
    elif number > 1000000:
        print("large positive")
    else:
        print("positive")

# Output
