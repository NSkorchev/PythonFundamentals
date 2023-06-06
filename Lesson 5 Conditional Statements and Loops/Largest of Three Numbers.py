# Read user input
number1 = int(input())
number2 = int(input())
number3 = int(input())
max_number = 0
# Logic
if number1 > number2 and number1 > number3:
    max_number = number1
elif number2 > number3 and number2 > number1:
    max_number = number2
else:
    max_number = number3

# Output
print(f"{max_number}")
print(max(number1, number2, number3))