# Read user input
lessons = input().split(", ")
# Logic

while True:
    command = input()
    if command == "course start":
        break

    action = command.split(":")[0]
    lesson = command.split(":")[1]

    if action == "Add" and lesson not in lessons:
        lessons.append(lesson)

    elif action == "Insert" and lesson not in lessons:
        index = int(command.split(":")[2])
        if index < len(lessons):
            lessons.insert(index, lesson)

    elif action == "Remove" and lesson in lessons:
        index = lessons.index(lesson) + 1
        lessons.remove(lesson)
        if len(lessons) - 1 >= index:
            if lessons[index].endswith("-Exercise"):
                lessons.remove(lessons[index])

    elif action == "Swap" and lesson in lessons:
        new_lesson = command.split(":")[2]

        if new_lesson in lessons:
            idx1 = lessons.index(lesson)
            idx3 = lessons.index(lesson) + 1
            idx2 = lessons.index(new_lesson)
            idx4 = lessons.index(new_lesson) + 1

            lessons[idx1] = new_lesson
            lessons[idx2] = lesson
            if len(lessons) - 1 >= max(idx4, idx3):
                if lessons[idx3].endswith("-Exercise"):
                    lessons.remove(lessons[idx3])
                    lessons.insert(idx4, f"{lesson}-Exercise")
                if lessons[idx4].endswith("-Exercise"):
                    lessons.remove(lessons[idx4])
                    lessons.insert(idx3, f"{new_lesson}-Exercise")
            else:
                continue

    elif action == "Exercise":
        if lesson in lessons:
            idx1 = lessons.index(lesson) + 1
            lessons.insert(idx1, f"{lesson}-Exercise")
        else:
            lessons.append(lesson)
            lessons.append(f"{lesson}-Exercise")

# Output
for index, lesson in enumerate(lessons, start=1):
    print(f"{index}.{lesson}")