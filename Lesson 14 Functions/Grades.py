# Read user input

# Logic
def grade_to_word(grade):
    if 2.00 <= grade <= 2.99:
        print("Fail")
    if 3.00 <= grade <= 3.49:
        print("Poor")
    if 3.50 <= grade <= 4.49:
        print("Good")
    if 4.50 <= grade <= 5.49:
        print("Very Good")
    if 5.50 <= grade <= 6.00:
        print("Excellent")
# Output
gr = float(input())
grade_to_word(gr)