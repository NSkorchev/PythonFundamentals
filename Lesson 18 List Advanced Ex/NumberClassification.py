# Read user input
numbers = [int(x) for x in input().split(", ")]
# # Logic
# positive_num = [x for x in numbers if x >= 0]
# negative_num = [x for x in numbers if x < 0]
# even_num = [x for x in numbers if x % 2 == 0]
# odd_num = [x for x in numbers if x % 2 != 0]
# # Output
# print(f"Positive: {','.join([str(x) for x in positive_num])}")
# print(f"Negative: {','.join([str(x) for x in negative_num])}")
# print(f"Even: {','.join([str(x) for x in even_num])}")
# print(f"Odd: {','.join([str(x) for x in odd_num])}")
positive_num = []
negative_num = []
even_num = []
odd_num = []

for num in numbers:
    if num >= 0:
        positive_num.append(num)
    else:
        negative_num.append(num)

    if num % 2 == 0:
        even_num.append(num)
    else:
        odd_num.append(num)

print(f"Positive: {', '.join([str(x) for x in positive_num])}")
print(f"Negative: {', '.join([str(x) for x in negative_num])}")
print(f"Even: {', '.join([str(x) for x in even_num])}")
print(f"Odd: {', '.join([str(x) for x in odd_num])}")