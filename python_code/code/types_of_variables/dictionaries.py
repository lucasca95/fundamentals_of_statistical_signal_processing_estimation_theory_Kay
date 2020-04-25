dict = {"key1": "value1", "key2": "value2"}

print(dict['key1'])

print(dict['key2'])
try:
    # No existe
    print(dict['key3'])
except KeyError as e:
    print("Valor de key no existe en el diccionario")
finally:
    print("FIN")
