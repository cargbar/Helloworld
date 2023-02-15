# Definir la funcion
def eliminar_elementos(lista_prueba, eliminar):
    for elementos in lista_prueba:
        if elementos == eliminar:
            lista_prueba.remove(eliminar)
    print(lista_prueba)


# Listas de pruebas
eliminar_elementos(["50", "30", "30", "60", "90", "60"], "60")
eliminar_elementos(["perro", "perro", "momo", "mona", "gato", "mona"], "mona")
