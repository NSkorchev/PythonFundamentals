# Create a program that receives two strings on a single line separated by a single space.
# Then, it prints the sum of their multiplied character codes as follows:
# multiply str1[0] with str2[0] and add the result to the total sum, then continue with the next two characters.
# If one of the strings is longer than the other, add the remaining character codes to the total sum without multiplication.

text = input().split()
str1 = text[0]
str2 = text[1]

min_len = min(len(str1), len(str2))
result = 0

for idx in range(min_len):
    str1_char = str1[idx]
    str2_char = str2[idx]
    result += ord(str1_char) * ord(str2_char)

for idx in range(min_len, len(str1)):
    result += ord(str1[idx])

for idx in range(min_len, len(str2)):
    result += ord(str2[idx])

print(result)