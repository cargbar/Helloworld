'''
Manejo de archivos. Los datos de los jugadores se guardan en archivos de texto
'''
from datetime import datetime

#Agrega el usuario
def get_player():
    #abre el archvo
    archivo=open("players.txt", "r")
    player_list= []
    for line in archivo:
        player_list.append(line.rstrip('\n'))
    #cierra el archivo
    archivo.close()
    return player_list

#Agrega las estadisticas del usuario seleccionado
def add_player_stats(playername,result):
    filename= playername.replace(" ","").lower()
    #abre el archivo
    archivo=open(f"{filename}-stats.txt", "a")
    dt= datetime.now()
    strdate= dt.strftime("%D, %B, %Y")
    archivo.write(f"{strdate}: {playername} {result} \n")
    #cierra el archivo
    archivo.close()

#Imprime los datos del archivo
def print_stats(name):
    archivo= open(f"{name}-stats.txt", "r")
    for x in archivo:
        print(x)
    archivo.close()