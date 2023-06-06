import re
# Read user input
pattern = r"\b_([a-zA-Z0-9]+)\b"
regex_pattern = re.compile(pattern)

result = []
line = input()
# Logic
variable = re.findall(regex_pattern, line)

# Output
print(",".join(variable))
