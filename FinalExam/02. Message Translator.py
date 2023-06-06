import re

pattern = r'\!(?P<command>[A-Z][a-z]{2,})\!\:\[(?P<message>[A-Za-z]{7,})\]'

count_strings = int(input())
for _ in range(count_strings):
    text = input()
    matches = re.match(pattern, text)
    if not matches:
        print("The message is invalid")
        continue

    command = matches.group("command")
    message = matches.group("message")
    ascii_nums = " ".join(str(ord(char)) for char in message)
    print(f"{command}: {ascii_nums}")