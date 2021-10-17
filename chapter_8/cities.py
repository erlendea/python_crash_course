def describe_cities(city, country = 'Norway'):
    print(f"{city.title()} is in {country.title()}.")


describe_cities('oslo')
describe_cities('røros')
describe_cities('reykjavik', 'iceland')
describe_cities(country='croatia', city='split')