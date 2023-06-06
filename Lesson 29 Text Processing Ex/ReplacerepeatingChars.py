line = input()
result = line[0]

for ch in line:
    if ch == result[-1]:
        continue
    result += ch

print(result)
