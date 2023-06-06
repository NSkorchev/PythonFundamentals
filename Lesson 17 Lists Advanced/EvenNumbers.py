# Read user input
# nums = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
# Logic
nums = list(map(int, input().split(", ")))
# Output
print(list(filter(lambda x: x % 2 == 0, nums)))
print([index for index in range(len(nums)) if nums[index] % 2 == 0])