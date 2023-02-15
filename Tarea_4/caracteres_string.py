# Definir la funcion
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


# Variables de prueba(Realizar la prueba con cada una de ellas)
string_test = "a6+e*8*2t"
# string_test = "++22"
# string_test = ""
# string_test = "a"
# string_test = [41614654d46a]
# string_test = "+"
# string_test = "8"
test = string_test
result = contar_digitos_letras_caract(test)
print("Cantidad de números: %i" % result[0])
print("Cantidad de letras: %i" % result[1])
print("Cantidad de caracteres especiales: %i" % result[2])
