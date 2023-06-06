# Read user input
words = input().split()
# Logic
result = [word for word in words if len(word) % 2 == 0]
# removed_sum = list(filter(lambda x: len(x) % 2 == 0, words)
# Output
for word in result:
    print(word)
