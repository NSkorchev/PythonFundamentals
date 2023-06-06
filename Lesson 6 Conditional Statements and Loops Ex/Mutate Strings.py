# Read user input
string1 = input()
string2 = input()

result = string1
# Logic
for idx in range (len(string1)):
    result = string2[:idx + 1] + string1[idx + 1:]

    if string1[idx] == string2[idx]:
        continue
    print(result)
# Output
