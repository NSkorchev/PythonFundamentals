# Read user input
single_string = input()
digits = ""
letters = ""
other = ""
# Logic
for char in single_string:
    if char.isdigit():
      digits += char
    elif char.isalpha():
        letters += char
    else:
        other += char
# Output
print(f"{digits}\n{letters}\n{other}")
