# Read user input
# action = "Hello"
# unique_el = set(action)
# print(len(action))
# print(set(action))
# print(len(unique_el))
year = int(input())
year += 1
year_as_string = str(year)
# Logic
while len(year_as_string) != len(set(year_as_string)):
    year_as_string = str(year)
# Output
print(year)