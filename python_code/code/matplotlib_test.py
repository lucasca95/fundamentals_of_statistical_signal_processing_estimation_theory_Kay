# matplotlib permite graficar datos.
import numpy as np 
from matplotlib import pyplot as plt
import pandas as pd

def recta():
    x = np.arange(-10, 11, 1)
    y = pow(x,2)
    return x, y

def graficar(x, y, title='', xlabel='x', ylabel='y', color=None, linewidth=2, linestyle='-', grid=True):
    plt.plot(x, y, color=color, linewidth=linewidth, linestyle=linestyle)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(grid)
    return plt

def barras(dict, sentido='|'):
    dict_keys = list(dict.keys())
    dict_values = list(dict.values())
    if sentido == '|':
        plt.bar(dict_keys, dict_values)
    elif sentido == '-':
        plt.barh(dict_keys, dict_values)
    else:
        raise ValueError('\n"sentido" sólo admite valores: "|" ó "-" \n')
    plt.grid(True)
    return plt


def scatter(x, y):
    plt.scatter(x,y)
    plt.grid(True)
    return plt

def histograma(iris):
    plt.hist(iris['petal_width'], bins=20)
    plt.grid(True)
    return plt

def main():
    onWindows = 1

    x, y = recta()
    # graficar(x,y).show()

    datos = {'Lucas':24,'Agustina':20,'Fiorela':20}
    # barras(datos).show()

    x = [5,2,7,6,9,4]
    y = [8,5,5,1,9,8]
    # scatter(x,y).show()

    if (onWindows):
        iris = pd.read_csv('csv_files/iris.csv')
    # histograma(iris).show()

    # NO ESTÁ FUNCIONANDO
    print(iris.boxplot(column='petal_width', by='variety'))
    

if __name__ == '__main__':
    main()