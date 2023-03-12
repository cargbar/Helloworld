### IMPORTANTE EJECUTAR CADA FUNCION UNA A UNA ###

# Eliminar elementos repetidos de una lista
def eliminar_elementos(lista_prueba, eliminar):
    for elementos in lista_prueba:
        if elementos == eliminar:
            lista_prueba.remove(eliminar)
    print(lista_prueba)


# Listas de pruebas, ejecutar cada una
# eliminar_elementos(["50", "30", "30", "60", "90", "60"], "60")
# eliminar_elementos(["perro", "perro", "momo", "mona", "gato", "mona"], "mona")


# Eliminar elementos repetidos de una lista
from functools import reduce
from pprint import pprint

# Lista de prueba, ejecutar cada una.
# lista_aa = ["perro", "perro", "momo", "mona", "gato", "mona"]
# lista_aa = ["50", "30", "30", "60", "90", "60"]
# Lista_prueba = reduce(lambda l, x: l if x in l else l + [x], lista_aa, [])
# print(Lista_prueba)


# Contar Caracteres de una strirngs
def contador_caracteres(text: str):
    contador = {}
    if isinstance(text, str):
        for letter in text:
            if letter.lower() in contador:
                contador[letter.lower()] += 1
            else:
                contador[letter.lower()] = 1

        pprint(contador)
    else:
        print("Error:Not a string argument")


# test_texto = "aertyuoo"
# test_texto = "PytjjehfihwighrhgrhhGHhhhhhhhh"
# test_texto = ""
# test_texto = [4464994494]
texto = test_texto
contador_caracteres(texto)


# Contar Caracteres de una strirngs
def contador_caracteres_map_lambda(text: str):
    contador = {}
    if isinstance(text, str):
        for letter in text:
            contador[letter.lower()] = sum(
                map(lambda x: 1 if x.lower() == letter.lower() else 0, text)
            )
        pprint(contador)
    else:
        print("Error:Not a string argument")


# Textos de prueba, ejecutar cada uno.
# contador_caracteres_map_lambda("dsadsadsad")
# contador_caracteres_map_lambda("dgdgdg--")
# contador_caracteres_map_lambda("mdwi781288176")
# contador_caracteres_map_lambda("nhuiwnbugbcwdbbhwd")


# Contador de Caracteres, Numeros y Caracteres especiales
def contar_digitos_letras_caract(texto):
    numeros = 0
    letras = 0
    caract_especiales = 0
    # Conteo Utilizando metodos de string
    for caracteres in texto:
        if caracteres.isdigit():
            numeros += 1
        elif caracteres.isalpha():
            letras += 1
        else:
            caract_especiales += 1
    return numeros, letras, caract_especiales


# Textos de prueba, ejecutar cada uno.
# string_test = "a6+e*8*2t"
# string_test = "++22"
# string_test = ""
# string_test = "a"
# string_test = [41614654d46a]
# string_test = "+"
# string_test = "8"
test = string_test
# result = contar_digitos_letras_caract(test)
# print("Cantidad de números: %i" % result[0])
# print("Cantidad de letras: %i" % result[1])
# print("Cantidad de caracteres especiales: %i" % result[2])


# Contador de Caracteres, Numeros y Caracteres especiales
def contar_digitos_letras_caract(texto):
    numeros = len(list(filter(lambda x: x.isdigit(), texto)))
    letras = len(list(filter(lambda x: x.isalpha(), texto)))
    caract_especiales = len(
        list(filter(lambda x: not x.isdigit() and not x.isalpha(), texto))
    )
    return numeros, letras, caract_especiales


# Textos de prueba, ejecutar cada uno.
# text = "1561654nijkdbcusbuui----3###"
# text = "buwefu12349-*/+--/*-*"
# text = "12a******"
## text = ""

x = contar_digitos_letras_caract(text)
n, l, c = contar_digitos_letras_caract(text)
print("numeros: {} letras: {} caracteres especiales: {}".format(n, l, c))
