# Definir la funcion
from pprint import pprint


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


test_texto = "aertyuoo"
# test_texto = "PytjjehfihwighrhgrhhGHhhhhhhhh"
# test_texto = ""
# test_texto = [4464994494]
texto = test_texto
contador_caracteres(texto)
