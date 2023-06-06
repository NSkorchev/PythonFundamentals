# Read user input
def increase_small(num, distance):
    for i in range(len(distance)):
        if distance[i] <= num:
            distance[i] += num
        else:
            distance[i] -= num
    return distance

distance_to_pokemon = list(map(int, input().split()))
# distance_to_pokemon1 = [int(x) for x in input().split()]
# distance_to_pokemon2 = list(filter(lambda x: x > 10, pokemon_list))
# distance_to_pokemon3 = list(map(lambda x: int(x), input().split()))
removed_sum = 0
#Logic
while len(distance_to_pokemon) != 0:
    idx = int(input())

    if idx < 0:
        idx = 0
        removed_value = distance_to_pokemon.pop(idx)
        distance_to_pokemon.insert(0, distance_to_pokemon[-1])
        removed_sum += removed_value
        distance_to_pokemon = increase_small(removed_value, distance_to_pokemon)


    elif idx >= len(distance_to_pokemon):
        idx = len(distance_to_pokemon) - 1
        removed_value = distance_to_pokemon.pop(idx)
        distance_to_pokemon.append(distance_to_pokemon[0])
        removed_sum += removed_value
        distance_to_pokemon = increase_small(removed_value, distance_to_pokemon)

    else:
        removed_value = distance_to_pokemon.pop(idx)
        removed_sum += removed_value
        distance_to_pokemon = increase_small(removed_value, distance_to_pokemon)

# Output
print(removed_sum)