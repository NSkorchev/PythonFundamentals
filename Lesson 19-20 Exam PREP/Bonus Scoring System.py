from math import ceil
# Read user input
students = int(input())
total_lectures = int(input())
additional_bonus = int(input())
# Logic
max_attendance = 0
for i in range(students):
    attendances = int(input())
    max_attendance = max(attendances, max_attendance)

total_bonus = 0
if total_lectures != 0:
    total_bonus =(max_attendance / total_lectures) * (5 + additional_bonus)
# Output
print(f'Max Bonus: {ceil(total_bonus)}.')
print(f'The student has attended {max_attendance} lectures.')
