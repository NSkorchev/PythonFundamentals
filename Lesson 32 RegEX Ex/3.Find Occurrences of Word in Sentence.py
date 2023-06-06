import re
# Read user input

text = input()
word = input()

# Logic
matches = re.findall(rf"\b{word}\b", text, re.IGNORECASE)
# Output
print(len(matches))