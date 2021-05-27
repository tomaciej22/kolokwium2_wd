import pandas
import numpy
import matplotlib.pyplot
#zad3 grupa B
df = pandas.read_csv('cars.csv', header=0, sep=';')

b = df[(df['Model year'] > 71) & (df['Model year'] < 78)].groupby(['Model year']).agg({'Model year': ['count']})

wykres = b.plot.bar()
matplotlib.pyplot.xticks(rotation=0)
matplotlib.pyplot.ylabel("Ilość aut")
matplotlib.pyplot.xlabel("Roczniki aut")
matplotlib.pyplot.title('Roczniki aut')
matplotlib.pyplot.show()
