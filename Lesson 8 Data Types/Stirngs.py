# Read user input
text = "X-DSPAM-Confidence:    0.8475"
y = text.find('0.')
z = text[y : y + 6]
num = float(z)
print(num)
# Logic

# Output
