def city_country(city,country):
    string = f'"{city.title()}, {country.title()}"'
    return string

name = city_country('oslo', 'norway')
print(name)

name = city_country('split', 'croatia')
print(name)

name = city_country('sidney', 'australia')
print(name)