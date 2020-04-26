# Pandas significa Panel Data.
# La herramienta permite manipular y analizar datos

# Una estructura de datos unidimensional se llama Objeto Serial
# Una estructura de datos multidimensional se llama Dataframe
import sys
import pandas as pd


def main():
    s1 = pd.Series([1,2,3,4,5])
    print(f'Serie 1: {s1}, de tipo {type(s1)}')
    print(f"Como se ve, los valores de un objeto pandas están rotulados con un índice. El índice puede ser cambiado")

    s1 = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
    print(f"Resultado: {s1}")

    s1 = pd.Series({'a':10,'b':20,'lucas':30,'z':40})
    print(f"Llamando a un objeto con un diccionario como parámetro pandas asocia la llave con el índice y el valor con el valor")
    print(f"Pandas con diccionario:\n{s1}")

    # Los dataframes son estructuras de datos etiquetadas bidimensionales
    # En Dataframes los elementos de una columna comparten el mismo tipo de dato
    estructura = {"Col1":['dato1_col1', 'dato2_col1'], "Col2":['dato1_col2', 'dato2_col2']}
    dataframe = pd.DataFrame(estructura)
    print(f"Un dataframe se ve así:\n{dataframe}\n", file=sys.stderr)


    # DataFrame In-Built Functions -> head(), shape(), tail(), describe()
    iris = pd.read_csv('./csv_files/iris.csv')
    cant_elem = 4
    print(f'Usando head() imprimimos los primeros {cant_elem} iris:\n{iris.head(cant_elem)}\n', file=sys.stderr)
    print(f'Usando tail() imprimimos los últimos {cant_elem} iris:\n{iris.tail(cant_elem)}\n', file=sys.stderr)
    print(f'Usando describe() vemos detalles de nuestro conjunto de datos iris:\n{iris.describe()}\n', file=sys.stderr)
    
    # .iloc[] -> Index LOCation
    # es usado para acceder a las filas y columnas de un dataframe
    print(f'Extraemos las primeras 3 filas y columnas 3 y 4 del dataframe:\n{iris.iloc[0:3,2:4]}\n', file=sys.stderr)
    print(f'Extraemos de los datos registros 1 y 2 sólo los atributos 0 y 3:\n{iris.iloc[1:3, [0,3]]}\n', file=sys.stderr)

    # También podemos obtener información de un dataframe a través del nombre de sus columnas y no por la posición
    # esto lo hacemos con .loc[]
    print(f'Extraemos de los datos registros del 1 al 5\nsólo los atributos sepal_length y sepal_width:\n{iris.loc[1:6, ("sepal_length", "petal_width")]}\n', file=sys.stderr)

    # Una sola fila
    print(f'Una sola fila del dataframe:\n{iris.iloc[10]}', file=sys.stderr)
    # Una sola columna
    print(f'Una sola columna del dataframe:\n{iris["sepal_length"]}', file=sys.stderr)

    # Devolver registros que cumplan una condición
    # dataframe[condición]
    print(f'Devuelvo los iris que tengan sepal_length mayor a 5.0:\n{iris[(iris["sepal_length"] > 5.0) & (True)]}', file=sys.stderr)



if __name__ == "__main__":
    main()