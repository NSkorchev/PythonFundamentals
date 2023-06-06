# line = input()
# part = line.split(':')
#
# for line in part[1:]:
#     if line:
#         symbol = line[0]
#         print(f':{symbol}')

line = input()

for idx in range(len(line)):
    ch = line[idx]
    if ch == ':' and idx + 1 < len(line):
        symbol = line[idx + 1]
        print(f':{symbol}')