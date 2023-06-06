# line = input()
# args = ""
# x = 0
#
# for idx in range(len(line)):
#     if line[idx] == '>':
#         x += int(line[idx + 1])
#         args += line[idx]
#     elif line[idx] != ">" and x > 0:
#         x -= 1
#     else:
#         args += line[idx]
#
# print(args)

line = input()
parts = line.split('>')
previous = 0

result = [parts[0]]
for part in parts[1:]:
    power = int(part[0])
    previous += power
    formated_part  = part[previous:]
    previous = max(previous - len(part), 0)
    result.append(formated_part)

print('>'.join(result))
