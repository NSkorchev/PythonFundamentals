# Read user input
sequences = input().split()
result = ""
# Logic
for sequence in sequences:
    length = len(sequence)
    result += sequence * length

# Output
print(result)
