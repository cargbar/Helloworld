lista_prueba = [
    1,
    2,
    3,
    5,
    4,
    3,
    4,
    2,
    1,
    8,
    9,
    0,
    1,
    3,
    4,
    7,
    8,
    9,
    11,
    10,
    21,
    34,
    11,
]
new_list = []
for i in lista_prueba:
    if i not in new_list:
        new_list.append(i)
print(new_list)
