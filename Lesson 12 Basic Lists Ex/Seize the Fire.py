# Read user input
fire_cells = input().split("#")
water = int(input())
# print(fire_cells)

valid_values = []
total_fire = 0
total_effort = 0
# Logic
for fire_cell in fire_cells:

    type_of_fire, cell_value = (fire_cell.split(" = "))
    cell_value = int(cell_value)
    # print(fire_cell)
    # print(type_of_fire)
    # print(cell_value)

    if type_of_fire == "High" and 81 <= cell_value <= 125:
        # High fire
        if cell_value <= water:
            valid_values.append(cell_value)
            total_effort += cell_value * 0.25
            water -= cell_value
            total_fire += cell_value

    elif type_of_fire == "Medium" and 51 <= cell_value <= 80:
        # Medium fire
        if cell_value <= water:
            water -= cell_value
            valid_values.append(cell_value)
            total_effort += cell_value * 0.25
            total_fire += cell_value

    elif type_of_fire == "Low" and 1 <= cell_value <= 50:
        # Low fire
        if cell_value <= water:
            water -= cell_value
            valid_values.append(cell_value)
            total_effort += cell_value * 0.25
            total_fire += cell_value

# Output
# print(valid_values)
print("Cells:")
for value in valid_values:
    print(f" - {value}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
