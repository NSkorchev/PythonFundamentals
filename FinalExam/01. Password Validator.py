import string

# Read user input
def is_valid_index(index, seq):
    return 0 <= index < len(seq)
password = input()

# Logic
while True:
    commands = input()
    if commands == "Complete":
        break

    if commands.startswith("Make"):
        command, argument, argument2 = commands.split()
        idx = int(argument2)
        if argument == "Upper" and is_valid_index(idx, password):
            password = password[:idx] + password[idx].upper() + password[idx+1:]
            print(password)
        elif argument == "Lower" and is_valid_index(idx, password):
            password = password[:idx] + password[idx].lower() + password[idx + 1:]
            print(password)

    elif commands.startswith("Insert"):
        command, argument, argument2 = commands.split()
        idx = int(argument)
        idx1 = argument2
        if is_valid_index(idx, password):
            password = password[:idx] + idx1 + password[idx:]
            print(password)

    elif commands.startswith("Replace"):
        command, argument, argument2 = commands.split()
        character = ord(argument)
        value = int(argument2)
        replace_char = chr(character + value)
        for char in password:
            if char == argument:
                password = password.replace(char, replace_char)
        print(password)

    elif commands.startswith("Validation"):
        if len(password) < 8:
            print("Password must be at least 8 characters long!")
        if not all(char.isalnum() or char == "_" for char in password):
            print("Password must consist only of letters, digits and _!")
        if not any(char in string.ascii_uppercase for char in password):
            print("Password must consist at least one uppercase letter!")
        if not any(char in string.ascii_lowercase for char in password):
            print("Password must consist at least one lowercase letter!")
        if not any(char in string.digits for char in password):
            print("Password must consist at least one digit!")

# Output
# "Password must be at least 8 characters long!"
# "Password must consist only of letters, digits and _!"
# "Password must consist at least one uppercase letter!"
# "Password must consist at least one lowercase letter!"
# "Password must consist at least one digit!"


