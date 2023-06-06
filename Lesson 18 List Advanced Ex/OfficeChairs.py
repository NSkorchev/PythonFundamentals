# Read user input
rooms = int(input())
free_chairs = 0
game_on = True
# Logic

for room in range(1, rooms + 1):
    chairs, guests = input().split()
    guests = int(guests)


    if guests > len(chairs):
        needed_charis = guests - len(chairs)
        print(f"{needed_charis} more chairs needed in room {room}")
        game_on = False
    else:
        free_chairs_row = len(chairs) - guests
        free_chairs += free_chairs_row
# Output
if game_on:
    print(f"Game On, {free_chairs} free chairs left")