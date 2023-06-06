# # Read user input
# num = int(input())
# # num_as_string = str(num)
# # new_num = ''
# # print(num_as_string)
# # # Logic
# for i in range(0, len(num_as_string) + 1):
#     if num_as_string[0] > num_as_string[1] and num_as_string[0] > num_as_string[2]:
#         new_num = num_as_string[0] + num_as_string[1] + num_as_string[2]
#     elif num_as_string[0] < num_as_string[1]:
#         new_num = num_as_string[1] + num_as_string[0]
# print(new_num)


# # Output
# lesson = input()
# n = str(lesson)
#
# m = sorted(n, reverse=True)
#
# for d, digit in enumerate(m):
#     print(digit, end="")

number = input()
for n in range(9, -1, -1):
    for i in number:
        if int(i) == int(n):
            print(n, end="")