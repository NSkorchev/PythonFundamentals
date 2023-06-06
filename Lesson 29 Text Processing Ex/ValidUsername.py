# Write a program that reads usernames on a single line (separated by ", ") and prints all valid usernames on separate lines.
# A valid username:
# •	has length between 3 and 16 characters inclusive
# •	can contain only letters, numbers, hyphens, and underscores
# •	has no redundant symbols before, after, or in between

from string import ascii_letters, digits

usernames = input().split(", ")
allowed_chars = ascii_letters + digits + "_" + "-"

for username in usernames:
    if len(username) <3 or len(username) > 16:
        continue

    forbidden_char = False

    for char in username:
        if char not in allowed_chars:
            forbidden_char = True
            break

    if forbidden_char:
        continue

    print(username)