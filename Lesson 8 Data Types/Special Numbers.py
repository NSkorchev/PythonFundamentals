# Read user input
n = int(input())
# Logic
for num in range(1, n + 1):
    is_special = False
    # num_str = str(num)
    sum_digits = 0
    # for char in num_str:
    #     sum_digits += int(char)
    digit = num
    while digit:
        last_num = digit % 10
        sum_digits += last_num
        digit = digit // 10

    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        is_special = True

    print(f"{num} -> {is_special}")
# Output
