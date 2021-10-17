rivers = {
    'nile': 'egypt',
    'glomma': 'norway',
    'volga': 'russia',
}

print("\nRivers and corresponding countries:")

for river, country in rivers.items():
    print(f"{river.title()} runs through {country.title()}.")

print("\nRivers:")
for river in rivers.keys():
    print(river.title())

print("\nCountries:")
for country in rivers.values():
    print(country.title())