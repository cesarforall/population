import re


def get_data_by_country(country, data):
    result = list(
        filter(lambda item: item['Country/Territory'] == country, data))
    if len(result) == 0:
        print(f"No tenemos datos de {country}")
    return result


def get_data_for_charts(headers, country_data):
    single_year_headers = []

    # Get year digits
    for item in headers:
        match = re.match(r'.*([1-2][0-9]{3})', item)
        if match is not None:
            # Then it found a match!
            # print(match.group(1))
            # print(type(match.group(1)))
            single_year_headers.append(match.group(1))

    # Get the entire population header name
    population_headers = []

    """    
    def get_header(year):
        for header in headers:
            if year in header:
                return header
    """

    for year in single_year_headers:
        # print(year)
        # header = get_header(year)
        for header in headers:
            if year in header:
                population_headers.append(header)

    # Filter population from country
    country_population = {}

    for population_header in population_headers:
        index = population_headers.index(population_header)
        country_population[single_year_headers[index]
                           ] = int(country_data[0][population_header])

    # print(country_population)

    year = country_population.keys()
    population = country_population.values()

    return year, population
