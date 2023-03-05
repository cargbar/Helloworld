'''
Manejo de los archivos con los datos del usuario seleccionado
'''
from datetime import datetime

#Agrega el usuario
def get_player():
    #abre el archvo
    archivo=open("players.txt", "r")
    players_list=[]
    for line in archivo:
        players_list.append(line.rstrip('\n'))
    #cierra el archivo
    archivo.close()
    return players_list

#Agrega las estadisticas del usuario
def add_player_stats(playername, result):
    filename= playername.replace(' ','').lower()
    #abre el archivo
    archivo= open(f"{filename}-stats.txt", "a")
    dt=datetime.now()
    strdate= dt.strftime("%D, %B, %Y")
    archivo.write(f"{strdate}: {playername} {result}\n")
    #cierra el archivo
    archivo.close()

#Imprime estadisticas del usuario
def print_stats(playername):
    filename= playername.replace(' ','').lower()
    #abre el archivo
    archivo= open(f"{filename}-stats.txt", "r")
    for x in archivo:
        print(x)
    #cierra el archivo
    archivo.close()