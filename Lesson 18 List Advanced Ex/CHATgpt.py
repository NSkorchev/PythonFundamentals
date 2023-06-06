def solve_task(task_description):
    if "sort numbers into lists of 10's" in task_description:
        task_description = task_description.replace("sort numbers into lists of 10's", "").strip()
        numbers = task_description.split(", ")
        numbers = [int(number) for number in numbers]
        groups = {}
        for number in numbers:
            group = (number // 10) * 10
            if group not in groups:
                groups[group] = []
            groups[group].append(number)
        result = []
        for group, numbers_in_group in groups.items():
            result.append(f"Group of {group}'s: {numbers_in_group}")
        return "\n".join(result)
    elif "fill atom shells" in task_description:
        task_description = task_description.replace("fill atom shells", "").strip()
        electrons = int(task_description)
        shells = []
        i = 1
        while electrons > 0:
            max_electrons_in_shell = 2 * i**2
            electrons_in_shell = min(electrons, max_electrons_in_shell)
            shells.append(electrons_in_shell)
            electrons -= electrons_in_shell
            i += 1
        return shells
    else:
        return "Unable to solve task. Please enter a valid task description."

while True:
    user_input = input("Enter a task description (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    else:
        result = solve_task(user_input)
        print(result)