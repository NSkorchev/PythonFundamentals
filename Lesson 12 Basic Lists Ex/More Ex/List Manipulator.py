# Read user input
list_of_numbers = list(map(int, input().split()))
command = input()
# Logic
while command != "end":
    command = command.split()
    manipulation = command[0]
    idx = command[1]

    if manipulation == "exchange":
        idx = int(idx)
        if idx > (len(list_of_numbers) - 1) or idx < 0:
            print("Invalid index")
        else:
            sub_list1 = list_of_numbers[:idx + 1]
            sub_list2 = list_of_numbers[idx + 1:]
            list_of_numbers = sub_list2 + sub_list1


    elif manipulation == "max":
        if idx == "odd":
            odds = list(filter(lambda x: x % 2 != 0, list_of_numbers))
            if len(odds) == 0:
                print("No matches")
            else:
                max_odd = max(odds)
                reverse_list = odds[::-1]
                for num in reverse_list:
                    if num == max_odd:
                        index = len(odds) - 1 - odds[::-1].index(num)
                        print(index)
                        break
        elif idx == "even":
            even = list(filter(lambda x: x % 2 == 0, list_of_numbers))
            if len(even) == 0:
                print("No matches")
            else:
                max_even = max(even)
                reverse_list = even[::-1]
                for num in reverse_list:
                    if num == max_even:
                        index = len(even) - 1 - even[::-1].index(num)
                        print(index)
                        break


    elif manipulation == "min":
        if idx == "odd":
            odds = list(filter(lambda x: x % 2 != 0, list_of_numbers))
            if len(odds) == 0:
                print("No matches")
            else:
                min_odd = min(odds)
                reverse_list = odds[::-1]
                for num in reverse_list:
                    if num == min_odd:
                        index = len(odds) - 1 - odds[::-1].index(num)
                        print(index)
                        break
        elif idx == "even":
            even = list(filter(lambda x: x % 2 == 0, list_of_numbers))
            if len(even) == 0:
                print("No matches")
            else:
                min_even = min(even)
                reverse_list = even[::-1]
                for num in reverse_list:
                    if num == min_even:
                        index = len(even) - 1 - even[::-1].index(num)
                        print(index)
                        break


    elif manipulation == "first":
        idx = int(idx)
        if command[2] == "odd":
            odds = list(filter(lambda x: x % 2 != 0, list_of_numbers))
            if len(odds) == 0:
                print("[]")
            elif idx > len(list_of_numbers):
                print("Invalid count")
            elif idx > len(odds):
                print(odds)
            else:
                print(odds[:idx])

        elif command[2] == "even":
            even = list(filter(lambda x: x % 2 == 0, list_of_numbers))
            if len(even) == 0:
                print("[]")
            elif idx > len(list_of_numbers):
                print("Invalid count")
            elif idx > len(even):
                print(even)
            else:
                print(even[:idx])

    elif manipulation == "last":
        idx = int(idx)
        if command[2] == "odd":
            odds = list(filter(lambda x: x % 2 != 0, list_of_numbers))
            if len(odds) == 0:
                print("[]")
            elif idx > len(list_of_numbers):
                print("Invalid count")
            elif idx > len(odds):
                print(odds)
            else:
                print(odds[idx:])

        elif command[2] == "even":
            even = list(filter(lambda x: x % 2 == 0, list_of_numbers))
            if len(even) == 0:
                print("[]")
            elif idx > len(list_of_numbers):
                print("Invalid count")
            elif idx > len(even):
                print(even)
            else:
                print(even[idx:])

    command = input()

# Output
print(list_of_numbers)