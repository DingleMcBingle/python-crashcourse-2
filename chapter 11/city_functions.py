def city_country(city, country, population=0):
    """Returns the name of a city and country"""
    name_location = (city + ', ' + country)
    if population:
        name_location += ' - population: ' + str(population)
    return name_location.title()