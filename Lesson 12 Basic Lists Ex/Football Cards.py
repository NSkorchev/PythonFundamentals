# Read user input
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
cards = input().split()

# Logic
for card in cards:
    team_name, player_num = card.split("-")
    player_num = int(player_num)

    if team_name == "A":
        if player_num in A:
            A.remove(player_num)
    elif team_name == "B":
        if player_num in B:
            B.remove(player_num)
    result = "Team A - {}; Team B - {}".format(len(A), len(B))
    if len(A) < 7 or len(B) < 7:
        result += "\nGame was terminated"
        break



# Output
print(result)