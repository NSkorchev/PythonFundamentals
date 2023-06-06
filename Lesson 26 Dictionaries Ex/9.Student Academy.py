next_rows = int(input())
students = {}

for idx in range(next_rows):
    student_name = input()
    grade = float(input())

    if student_name not in students:
        students[student_name] = []

    students[student_name].append(grade)

for name, grades in students.items():
    average_grade = sum(grades) / len(grades)
    if average_grade < 4.5:
        continue

    print(f"{name} -> {average_grade:.2f}")

