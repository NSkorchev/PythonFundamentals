line = input()
encrypted_line = ''

for ch in line:
    ceaser_ch = ord(ch) + 3
    encrypted_line += chr(ceaser_ch)

print(encrypted_line)

# encrypted_line = ''.join([chr(ord(ch) + 3) for ch in line])