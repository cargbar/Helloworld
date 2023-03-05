'''
En este archivo se encuentran distintas funciones que se necesitan a lo largo del juego
'''
import Hand as H
import deck as D
import Game as G
import agregar_archivo as A


# # Funciones para mostrar Cartas
# def show_some(player,dealer):
#     print("\nDealer's Hand")
#     print("<card hidden>")
#     print(' ', dealer.cards[1])
#     print("\nPlayer's Hand: ", *player.cards, sep= '\n')

# def show_all(player,dealer):
#     print("\nDealer's Hand:", *dealer.cards, sep="\n")
#     print("Dealer's Hand =",dealer.value)
#     print("\nPlayer's Hand: ", *player.cards, sep= '\n')
#     print("Player's Hand = ", player.value)

#Funciones relacionadas al pedir el usuario
def create_player():
    all_players= A.get_player()
    name= ""
    while True:
        #pide al usuario el jugador
        name=input("\tIngrese el nombre del jugador: ")
        if name in all_players:
            print("\tEl jugador ya existe")
        else:
            break
    #guarda el jugador en el archivo
    archivo= open("players.txt", "a")
    archivo.write(name + "\n")
    archivo.close()

    return name

def select_player():
    all_players= A.get_player()
    if len(all_players)== 0:
        print("\tNo hay jugadores para seleccionar")
        return create_player()
    else:
        print("\tJugadores disponibles")
        for i in range(0, len(all_players)):
            print(f'{i+1}- {all_players[i]}')
    #pide al usuario seleccionar un jugador de la lista
    selected_player= int(input("\tDigite el numero del jugador que desea seleccionar: ")) -1
    return all_players[selected_player]

def handle_player_select():
    #input para que el usuario escoja si desea agregar un jugador o seleccionar uno
    selectorcreate=int(input("\t\t1)Agregar un nuevo player\n\t\t2)Seleccionar un player existente\n"))
    while True:
        if selectorcreate==1:
            return create_player()
        elif selectorcreate==2:
            return select_player()
        else:
            print("Error, seleccione una opcion válida")
 


# Funciones relacionadas al estado del juego
def in_game():
    print("Sigue en juego 🂸...")


def game_over():
    print("El juego ha acabado")

#Funcion para mostrar las estadisticas del usuario seleccionado
def show_stats():
    all_players= A.get_player()
    print("Jugadores disponibles")
    for i in range(0, len(all_players)):
        print(f'{i+1}- {all_players[i]}')
    chosen_player= int(input("Digite el numero del jugador del que desea ver las estadisticas: ")) -1
    A.print_stats(all_players[chosen_player])

#Funciones relacionadas a pedir mas o quedarse
def hit(hand, deck):
    hand.add_card(deck.deal())
def hit_stand(hand, deck):
        global playing

        while True:
            opcion= input("\nDesea pedir más o se queda? Ingrese 'p' para pedir o 'q' para quedarse: \n" )
            
            if opcion[0].lower()=='p':
                hit(hand, deck)
            elif opcion[0].lower()=='q':
                print('\nEl jugador se queda, Dealer jugando')
                playing=False
            else:
                print('\nError, seleccione una opcion valida')
                continue
            break