# Definir la funcion
def lista_tupla(numeros):
    lista_numeros = numeros.split(",")
    tupla_numeros = tuple(lista_numeros)
    print(f"Lista:{lista_numeros}\nTupla: {tupla_numeros}")


lista_tupla("6,7,90,11,")
