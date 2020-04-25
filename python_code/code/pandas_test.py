# Pandas significa Panel Data.
# La herramienta permite manipular y analizar datos

# Una estructura de datos unidimensional se llama Objeto Serial
# Una estructura de datos multidimensional se llama Dataframe

import pandas as pd


def main():
    s1 = pd.Series([1,2,3,4,5])
    print(f"Serie 1: {s1}, de tipo {type(s1)}")
    print(f"Como se ve, los valores de un objeto pandas están rotulados con un índice. El índice puede ser cambiado")

    s1 = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
    print(f"Resultado: {s1}")

    s1 = pd.Series({'a':10,'b':20,'lucas':30,'z':40})
    print(f"Llamando a un objeto con un diccionario como parámetro pandas asocia la llave con el índice y el valor con el valor")
    print(f"Pandas con diccionario:\n{s1}")

if __name__ == "__main__":
    main()