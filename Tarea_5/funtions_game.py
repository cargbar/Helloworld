'''
En este archivo se encuentran distintas funciones que se necesitan a lo largo del juego
'''
import Hand as H
import Deck as D
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
        name=input("\tIngrese el nombre del jugador: ")
        if name in all_players:
            print("\tEl jugador ya existe")
        else:
            break

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
    selected_player= int(input("\tDigite el numero del jugador que desea seleccionar: ")) -1
    return all_players[selected_player]

def handle_player_select():
    selectorcreate=int(input("\t\t1)Agregar un nuevo player\n\t\t2)Seleccionar un player existente\n"))
    while True:
        if selectorcreate==1:
            return create_player()
        elif selectorcreate==2:
            return select_player()
        else:
            print("Error, seleccione una opcion válida")
 

#Funciones relacionadas al estado del juego
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
def hit_stand(players_hand, deck):
    for hand in players_hand:
        while True:
            opcion= input("\nDesea pedir más o se queda? Ingrese 'p' para pedir o 'q' para quedarse: \n" )
            if opcion[0].lower()=='p':
                hand.add_card(deck.deal())
            elif opcion[0].lower()=='q':
                print('El jugador se queda, Dealer jugando')
                playing=False
            else:
                print('Error, seleccione una opcion valida')
                continue
            break

#Escenarios que definene quien gana o pierde
def game_scenarios(name, players_hand, dealer_hand):
        for hand in players_hand:
            if hand.value> 21:
                G.Game.player_loses(name, "Perdió")
                break
            if hand.value<= 21:
                while dealer_hand.value< 17:
                    dealer_hand.add_card(D.Deck.deal())
                    #Muestra las manos
                    H.Hand.show_hand(False)
                    if dealer_hand.value> 21:
                         print("El dealer ha perdido")
                         G.Game.player_wins(name, "Ganó")
                    elif dealer_hand.value > hand:
                         print("El dealer ha ganado")
                         G.Game.player_loses(name, "Perdió")
                    elif dealer_hand < hand:
                         print("El dealer ha perdido")
                         G.Game.player_wins(name, "Ganó")
                    else:
                        print("Ha ocurrido un empate")