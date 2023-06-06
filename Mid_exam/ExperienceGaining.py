# Read user input
experience_needed = float(input())
count_batles = int(input())
counter = 0
successfull = False
# Logic
for i in range(1, count_batles + 1):
    experience_earned = int(input())

    if i % 3 == 0:
        experience_earned *= 1.15
    if i % 5 == 0:
        experience_earned *= 0.9
    if i % 15 == 0:
        experience_earned *= 1.05

    experience_needed -= experience_earned
    counter += 1

    if experience_needed <= 0:
        successfull = True
        break

# Output
if successfull:
    print(f"Player successfully collected his needed experience for {counter} battles.")
else:
    print(f"Player was not able to collect the needed experience, {experience_needed:.2f} more needed.")