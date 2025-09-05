import utils
import read_csv
import charts

def run():
    data = read_csv.get_read_csv('./data.csv')
    data = list(filter(lambda item : item['Continent'] == 'South America',data))

    countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    charts.generate_pie_chart(countries, percentages)

    # country = input('Type Country => ')
    # result = utils.population_by_country(data, country)

    # if len(result) > 0:
    #   country = result[0]
    #   labels, values = utils.get_population(country)
    #   charts.generate_bar_chart(labels, values)

# punto de inicio o punto de entrada de un programa o aplicación
# entry point
if __name__ == '__main__':
    run()

"""
Esta estructura se utiliza para asegurarse de que el código dentro del bloque 
if __name__ == '__main__': solo se ejecute cuando el archivo de Python se 
ejecuta directamente como un programa y no cuando se importa como un módulo en otro programa.
"""