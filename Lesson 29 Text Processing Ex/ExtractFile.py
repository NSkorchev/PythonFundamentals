# file_path = input().split('\\')
#
# for part in file_path:
#     if part == file_path[-1]:
#         result = part.split('.')
#         # template = result[0]
#         extension = result[-1]
#         print(f"File name: {'.'.join(result)}")
#         print(f"File extension: {extension}")
#         break
file_path = input().split('\\')

part = file_path[-1]
result = part.split('.')
# template = result[0]
extension = result.pop()
print(f"File name: {'.'.join(result)}")
print(f"File extension: {extension}")
