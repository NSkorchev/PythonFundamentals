# Read user input
n = int(input())

negative = []
positive = []

# Logic
for i in range(0,n):
    number = int(input())
    if number < 0:
        negative.append(number)
    else:
        positive.append(number)

count_positives = len(positive)
# Output
print(positive)
print(negative)
print(f"Count of positives: {count_positives}")
print(f"Sum of negatives: {sum(negative)}")
