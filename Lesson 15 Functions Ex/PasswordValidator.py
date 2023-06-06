# Read user input
def pass_validation(password):
    errors = []
    if not pass_validation_len(password):
        errors.append("Password must be between 6 and 10 characters")
    if not pass_validation_alnum(password):
        errors.append("Password must consist only of letters and digits")
    if not pass_validation_digits(password):
        errors.append("Password must have at least 2 digits")

    return errors

def pass_validation_len(password):
    return 6 <= len(password) <= 10


def pass_validation_alnum(password):
    return password.isalnum()


def pass_validation_digits(password):
    digit_counter = 0
    for digit in password:
        if digit.isdigit():
            digit_counter += 1

    return digit_counter >= 2


pass_input = input()

# Logic
# Output
errors = pass_validation(pass_input)
if len(errors):
    for error in errors:
        print(error)
else:
    print("Password is valid")