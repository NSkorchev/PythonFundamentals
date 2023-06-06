# Read user input
budget = int(input())
# Logic
while budget >= 0:
    prices = input()
    if prices == 'End':
        print("You bought everything needed.")
        break
    budget -= int(prices)
else:
    print("You went in overdraft!")
# Output