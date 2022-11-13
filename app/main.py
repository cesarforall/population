import my_tools

file = '../world_population.csv'


def run():
    print('Se inició el módulo main del paquete app')
    headers, countries = my_tools.csv_tools.read_csv(file)
    # print(headers)

    # Get a country from user
    #country = 'Spain'
    country = input('Escribe un país: ')
    country_data = my_tools.utils.get_data_by_country(country, countries)
    # print(country_data)

    year, population = my_tools.utils.get_data_for_charts(
        headers, country_data)
    # print(year)
    # print(population)

    type_chart = input("""Selecciona un tipo de gráfica:
    1 - Bar chart
    2 - Pie chart
    : """)

    if type_chart == '1':
        my_tools.charts.print_bar_chart(year, population)

    elif type_chart == '2':
        my_tools.charts.print_pie_chart(year, population)
    else:
        print(f"{type_chart} no está en las opciones")

    wpp = {}

    for country in countries:
        wpp[country['Country/Territory']] = country['World Population Percentage']

    #print(wpp)

    my_tools.charts.print_pie_chart(wpp.values(), wpp.keys())


if __name__ == '__main__':
    run()
