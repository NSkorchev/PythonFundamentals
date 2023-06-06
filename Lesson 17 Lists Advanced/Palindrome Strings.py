# Read user input
words = input().split()
searched_palindrome = input()
palindromes = []
# Logic
for word in words:
    if word == "".join(reversed(word)):
        palindromes.append(word)

# Output
print(f"{palindromes}")
print(f"Found palindrome {palindromes.count(searched_palindrome)} times")