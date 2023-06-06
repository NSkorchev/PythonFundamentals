countries = input().split(", ")
capitals = input().split(", ")

dictionary = {countries[idx]: capitals[idx] for idx in range(len(countries))}

for countries, capitals in dictionary.items():
    print(f"{countries} -> {capitals}")

# for idx in range(len(countries)):
#     country = countries[idx]
#     capital = capitals[idx]
#     capital_country[country] = capital