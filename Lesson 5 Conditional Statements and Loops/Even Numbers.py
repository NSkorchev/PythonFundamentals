# Read user input
n = int(input())
even = True
# Logic
for i in range(n):
    num = int(input())
    if num % 2 == 1:
        even = False
        print(f"{num} is odd!")
        break
# Output
if even == True:
    print("All numbers are even.")