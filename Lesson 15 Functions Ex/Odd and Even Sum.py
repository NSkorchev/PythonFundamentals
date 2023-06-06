# Read user input
num = input()

def sum_digit():
    sum_even = 0
    sum_odd = 0
    for digit in num:
        digit = int(digit)
        if digit % 2 == 0:
            sum_even += digit
        else:
            sum_odd += digit
    return(f"Odd sum = {sum_odd}, Even sum = {sum_even}")
# Logic
# Output
print(sum_digit())