# Read user input
def perfect_number(a):
    divisors = [d for d in range(1, a) if a % d == 0]
    aliquot_sum = sum(divisors)
    if aliquot_sum == a:
        print("We have a perfect lesson!")
    else:
        print("It's not so perfect.")


number = int(input())
# Logic
perfect_number(number)
# Output
