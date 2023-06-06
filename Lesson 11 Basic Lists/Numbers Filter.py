# Read user input
n = int(input())
positive_nums = []
negative_nums = []
even_nums = []
odd_nums = []
# Logic
for i in range(0, n):
    number = int(input())

    if number >= 0 :
        positive_nums.append(number)
    else:
        negative_nums.append(number)
    if number % 2 == 0:
        even_nums.append(number)
    else:
        odd_nums.append(number)

command = input()

# Output
if command == 'even':
    print(even_nums)
elif command == 'odd':
    print(odd_nums)
elif command == 'positive':
    print(positive_nums)
elif command == 'negative':
    print(negative_nums)