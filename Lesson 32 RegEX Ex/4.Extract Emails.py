import re
# Read user input
pattern = r"\s[A-Za-z\d][\-.\w\d]*@[A-Za-z][\-A-Za-z]*[A-Za-z]\.[A-Za-z]+[\.A-Za-z]*\b"
regex_pattern = re.compile(pattern)
text = input()

# Logic
matches = re.findall(regex_pattern, text)
# Output
for mail in matches:
    result = str(mail.strip())
    print(result)