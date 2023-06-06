# import math
# # Read user input
#
#
# def distance(a, b, c, d):
#     distance = math.sqrt((c - a) ** 2 + (d - b) ** 2)
#     return distance
#
#
# max_length = 0
# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())
# x1_ = None
# y1_ = None
# x2_ = None
# y2_ = None
# # Logic
# for i in range(2):
#
#     line_length = distance(x1, y1, x2, y2)
#     if line_length >= max_length:
#         max_length = line_length
#         x1_ = math.floor(x1)
#         y1_ = math.floor(y1)
#         x2_ = math.floor(x2)
#         y2_ = math.floor(y2)
#     if i == 1:
#         break
#
#     x1 = float(input())
#     y1 = float(input())
#     x2 = float(input())
#     y2 = float(input())
#
# # Output
# print(f"({x2_}, {y2_})({x1_}, {y1_})")

import math
from math import floor

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

def distance(_x1, _y1, _x2, _y2):
    line_length = math.sqrt((_x2 - _x1) ** 2 + (_y2 - _y1) ** 2)
    return line_length

x1y1 = distance(x1, y1, 0, 0)
x2y2 = distance(x2, y2, 0, 0)
x3y3 = distance(x3, y3, 0, 0)
x4y4 = distance(x4, y4, 0, 0)

line_1 = x1y1 + x2y2
line_2 = x3y3 + x4y4

if line_1 >= line_2:
    if x1y1 <= x2y2:
        print(f'({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})')
    else:
        print(f'({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})')
if line_1 < line_2:
    if x3y3 <= x4y4:
        print(f'({floor(x3)}, {floor(y3)})({floor(x4)}, {floor(y4)})')
    else:
        print(f'({floor(x4)}, {floor(y4)})({floor(x3)}, {floor(y3)})')