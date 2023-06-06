# Read user input
n = int(input())
# Logic
for i in range(n):
    code = int(input())
    if code == 88:
        print('Hello')
    elif code == 86:
        print("How are you?")
    elif code < 88:
        print("GREAT!")
    else:
        print("Bye.")
# Output
