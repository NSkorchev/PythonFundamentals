# Read user input
def data_types(type_a, a):
    if type_a == "int":
        a = int(a) * 2
    elif type_a == "string":
        a = "$" + a + "$"
    elif type_a == "real":
        a = f"{float(a) * 1.5:.2f}"
    return a

line_type = input()
line = input()

# Logic
result = data_types(line_type, line)

# Output
print(result)