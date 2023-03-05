# Agrega el usuario
def agregar_player(name):
    # abre el archvo
    archivo = open("game_data.txt", "a")
    archivo.write(f"El jugador {name}")
    archivo.write(",")
    # cierra el archivo
    archivo.close()


# Agrega las partidas ganadas
def agregar_wins(wins):
    # abre el archvo
    archivo = open("game_data.txt", "a")
    archivo.write(f"Ha ganado {wins} partidas")
    archivo.write(",")
    # cierra el archivo
    archivo.close()


# Agrega las partidas perdidas
def agregar_loses(loses):
    # abre el archvo
    archivo = open("game_data.txt", "a")
    archivo.write(f"Y ha perdido {loses} partidas")
    archivo.write("\n")
    # cierra el archivo
    archivo.close()
