import pandas as pd
import matplotlib.pyplot as plt
import os

car_path = os.path.abspath(os.path.join(os.path.dirname("__file__"), 'users'))
file_path = os.path.join(car_path, 'registro_partidas.csv')

datos = pd.read_csv(file_path)


def level_graphic():
    """ Porcentaje de partidas por nivel. """

    plt.clf()

    facil = datos[(datos['estado'] == 'finalizada') & (datos['nivel'] == 'Facil')]['nivel'].count()
    normal = datos[(datos['estado'] == 'finalizada') & (datos['nivel'] == 'Normal')]['nivel'].count()
    dificil = datos[(datos['estado'] == 'finalizada') & (datos['nivel'] == 'Dificil')]['nivel'].count()

    data_dibujo = [facil, normal, dificil]
    etiquetas = ['Facil', 'Normal', 'Dificil']
    plt.pie(data_dibujo, labels=etiquetas, autopct='%1.1f%%', shadow=True, startangle=90, labeldistance=1.1)
    plt.legend(etiquetas)
    plt.title('Porcentaje de partidas finalizadas por dificultad')
    plt.show()

