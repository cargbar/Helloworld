# Notas de clase
sample_dict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {"physics": 70, "history": 80, "math": 90},
        }
    }
}


def notas_de_clase(dict):
    nombre = dict["class"]["student"]["name"]
    fisica = dict["class"]["student"]["marks"]["physics"]
    historia = dict["class"]["student"]["marks"]["history"]
    mate = dict["class"]["student"]["marks"]["math"]
    promedio = (fisica + historia + mate) / 3
    return {"name": nombre, "avg": promedio}


# print(notas_de_clase(sample_dict))
