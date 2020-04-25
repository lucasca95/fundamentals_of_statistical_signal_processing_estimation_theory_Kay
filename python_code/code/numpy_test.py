# NumPy significa Numerical Python
# Proporciona arreglos multidimensionales de objetos y funciones para operarlos.

# np es un alias
import numpy as np 

print("NumPy imported successfuly!")

# arreglo unidimensional
vec = np.array([10, 20, 30, 40])
print(vec)

matriz = np.array([[10, 20, 30, 40], [40, 30, 20, 10]])
print(matriz)

vec_ceros = np.zeros((1, 2))
print(vec_ceros)

matriz_ceros = np.zeros((5, 5))
print(matriz_ceros)

vec_igual_valor = np.full((1,2),10)
print(vec_igual_valor)

matriz_igual_valor = np.full((3,3),7)
print(matriz_igual_valor)

inicio = 10
fin = 20
paso = 2

vec_rango = np.arange(inicio,fin+1)
print(vec_rango)

vec_rango_2 = np.arange(inicio,fin+1,paso)
print(vec_rango_2)

desde_num = 1
hasta_num = 101
cant_valores = 5
vec_aleatorio = np.random.randint(desde_num,hasta_num,cant_valores)
print(vec_aleatorio)
print(vec_aleatorio[0])

# corroborar filas y columnas de un objeto narray
matriz = np.array([[1,2,3,4],[5,6,7,8]])
print(matriz)
print(matriz.shape)
# girar matriz
matriz.shape = (4,2)
print(matriz)

# Sumar arreglos numpy
n1 = np.array([10,20, 30])
n2 = np.array([30,40, 50])
print(f"La suma de todos los valores de ambos arreglos da: {np.sum([n1, n2])}")
print(f"La suma vertical de los valores de ambos arreglos da: {np.sum([n1, n2], axis=0)}")
print(f"La suma horizontal de los valores de ambos arreglos da: {np.sum([n1, n2], axis=1)}")

# juntar arreglos numpy
print(f"Juntando verticalmente {n1} y {n2} con VerticalStack obtenemos:\n{np.vstack((n1, n2))}\n")
print(f"Juntando horizontalmente {n1} y {n2} con HorizontalStack obtenemos:\n{np.hstack((n1, n2))}\n")
print(f"Juntando por columnas {n1} y {n2} obtenemos:\n{np.column_stack((n1, n2))}")

