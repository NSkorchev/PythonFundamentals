# Read user input
key = int(input())
lines = int(input())
decripted_letter = None
result = ""
# Logic

for i in range(lines):
    letter = input()
    decripted_letter = chr(key + ord(letter))
    result += decripted_letter

# Output
print(result)