lessons = input().split(", ")
exercises = [f"{lesson}-Exercise" for lesson in lessons]
course_schedule = lessons + exercises

command = input()
while command != "course start":
    action = command.split(":")[0]
    lesson = command.split(":")[1]

    if action == "Add":
        if lesson not in course_schedule:
            course_schedule.append(lesson)
            exercises.append(f"{lesson}-Exercise")

    elif action == "Insert":
        index = int(command.split(":")[2])
        if lesson not in course_schedule:
            course_schedule.append(lesson)
            exercises.append(f"{lesson}-Exercise")
        if index >= 0 and index < len(course_schedule) and lesson not in course_schedule:
            course_schedule.insert(index, lesson)
            exercises.insert(index + 1, f"{lesson}-Exercise")

    elif action == "Remove":
        if lesson in course_schedule:
            lesson_index = course_schedule.index(lesson)
            course_schedule.remove(lesson)
            if course_schedule[lesson_index].endswith("-Exercise"):
                exercises.remove(course_schedule[lesson_index])

    elif action == "Swap":
        second_lesson = command.split(":")[2]
        if lesson in course_schedule and second_lesson in course_schedule:
            first_index = course_schedule.index(lesson)
            second_index = course_schedule.index(second_lesson)
            course_schedule[first_index], course_schedule[second_index] = course_schedule[second_index], \
                                                                          course_schedule[first_index]
            if course_schedule[first_index].endswith("-Exercise") or course_schedule[second_index].endswith(
                    "-Exercise"):
                exercise_index = course_schedule.index(course_schedule[first_index].replace("-Exercise", ""))
                exercises[exercise_index], exercises[exercise_index + 1] = exercises[exercise_index + 1], exercises[
                    exercise_index]

    elif action == "Exercise":
        if lesson in course_schedule:
            lesson_index = course_schedule.index(lesson)
            if not course_schedule[lesson_index].endswith("-Exercise"):
                exercise_index = lesson_index + 1
                course_schedule.insert(exercise_index, f"{lesson}-Exercise")
                exercises.insert(exercise_index, f"{lesson}-Exercise")
        else:
            course_schedule.append(lesson)
            exercises.append(f"{lesson}-Exercise")

    command = input()

for index, lesson in enumerate(course_schedule, start=1):
    print(f"{index}.{lesson}")