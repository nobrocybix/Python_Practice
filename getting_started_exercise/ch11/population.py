def get_city_country_name(city, country, population=''):
    city = city.title()
    country = country.title()
    population = population

    output_city_country_name = city + ", " + country + " - population " + str(population)
 
    return output_city_country_name