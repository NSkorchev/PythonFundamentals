# Read user input
def factorial_division(a, b):
    def factorial(num):
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result

    if a == 0:
        return f"{1:.2f}"
    else:
        return f"{factorial(a) / factorial(b):.2f}"

# Logic
num1 = int(input())
num2 = int(input())
# Output
print(factorial_division(num1, num2))