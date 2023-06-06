courses = {}

line = input()

while line != "end":
    course_input = line.split(" : ")
    course_name = course_input[0]
    student_name = course_input[1]

    if course_name not in courses:
        courses[course_name] = [student_name]
    else:
        courses[course_name].append(student_name)
    line = input()

for key, value in courses.items():
    print(f"{key}: {len(value)}")
    for i in value:
        print(f"-- {i}")
