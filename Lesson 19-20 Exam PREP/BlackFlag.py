# Read user input
days_at_sea = int(input())
plunder_per_day = int(input())
expected_plunder = int(input())
total_plunder = 0
# Logic
for i in range(1, days_at_sea + 1):

    total_plunder += plunder_per_day
    if i % 3 == 0:
        total_plunder += (0.5 * plunder_per_day)
    if i % 5 == 0:
        total_plunder *= 0.7


# Output
if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {total_plunder / expected_plunder * 100:.2f}% of the plunder.")