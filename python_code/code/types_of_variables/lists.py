l1 = [1, 'a', True, 23.0, 'Hola']
print(l1[2])
l1[2] = False
print(l1[2])

# Agregar elemento al final de la lista
l1.append([1, 2, 6])
print(l1)

# Obtener y quitar el último elemento de la lista
elem = l1.pop()
print(f'El último elemento era: {elem}.\n Ahora la lista tiene: {l1}')

