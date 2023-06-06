# Read user input
secret_message = input().split()
decoded = []

# Logic

for word in secret_message:
    while word[0].isdigit():
        num_as_str.append(word[0])
        secret_message.pop(0)

print(num_as_str)
print(secret_message)

# Output
