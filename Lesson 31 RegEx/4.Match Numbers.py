import re
pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

text = input()
regex_pattern = re.compile(pattern)
numbers = re.finditer(regex_pattern, text)

for num in numbers:
    print(num.group(), end=" ")