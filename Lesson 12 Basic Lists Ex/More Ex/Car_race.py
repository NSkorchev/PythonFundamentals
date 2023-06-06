times = [int(x) for x in input().split()]

finish_line = int(len(times) // 2)
first_car = 0
second_car = 0
total_time = 0
# Logic
for i in range(0, finish_line):
    if times[i] == 0:
        first_car *= 0.8
    first_car += times[i]
for i in range(finish_line + 1, len(times)):
    if times[i] == 0:
        second_car *= 0.8
    second_car += times[i]

if first_car < second_car:
    winner = "left"
    total_time = first_car
else:
    winner = "right"
    total_time = second_car

# Output
print(f"The winner is {winner} with total time: {total_time:.1f}")
#
# numbers = list(map(int, input().split()))
#
# car_one_time = 0
# car_two_time = 0

# middle_index = len(numbers) // 2 + 1
#
# for i in numbers[0:middle_index - 1]:
#     car_one_time += int(i)
#     if int(i) == 0:
#         car_one_time *= 0.80  # при този начин на модифициране на променливата, дава 100 от 100
#
# for j in numbers[len(numbers):middle_index - 1:-1]:
#     car_two_time += int(j)
#     if int(j) == 0:
#         car_two_time *= 0.80  # при този начин на модифициране на променливата, дава 100 от 100
#
# total_time = 0
# winner = ""
#
# if car_one_time > car_two_time:
#     winner = "right"
#     print(f"The winner is {winner} with total time: {car_two_time:.1f}")
# elif car_one_time < car_two_time:
#     winner = "left"
#     print(f"The winner is {winner} with total time: {car_one_time:.1f}")