from math import floor
# Read user input
def center_point(a, b, c, d):
    if a ** 2 + b ** 2 >= c ** 2 + d ** 2:
        return f"({floor(c)}, {floor(d)})"
    elif a ** 2 + b ** 2 < c ** 2 + d ** 2:
        return f"({floor(a)}, {floor(b)})"


# Logic
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

result = center_point(x1, y1, x2, y2)
# Output
print(result)