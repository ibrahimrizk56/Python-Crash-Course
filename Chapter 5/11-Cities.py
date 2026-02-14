# 6-11. Cities: Make a dictionary called cities. Use the names of three cities
# as keys in your dictionary. Create a dictionary of information about each city
# and include the country that the city is in, its approximate population, and
# one fact about that city. The keys for each city’s dictionary should be
# something like country, population, and fact. Print the name of each city and
# all of the information you have stored about it.

cities = {
    "Cairo": {
        "country": "Egypt",
        "population": 20000000,
        "fact": "Cairo is home to the Great Pyramids of Giza."
    },
    "Tokyo": {
        "country": "Japan",
        "population": 37000000,
        "fact": "Tokyo is the largest metropolitan area in the world."
    },
    "Paris": {
        "country": "France",
        "population": 11000000,
        "fact": "Paris is known as the City of Light."
    }
}

for city , values in cities.items():
    print(f"{city}:")
    for info , value in values.items():
        print(f"{info}: {value}")
    print("")