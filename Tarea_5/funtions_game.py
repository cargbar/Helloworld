import Hand as H
import Deck as D
import Player as P
import agregar_archivo as A

# Funciones para mostrar Cartas
def show_some(player,dealer):
    print("\nDealer's Hand")
    print("<card hidden>")
    print(' ', dealer.cards[1])
    print("\nPlayer's Hand: ", *player.cards, sep= '\n')

def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep="\n")
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep= '\n')
    print("Player's Hand = ", player.value)

#Funcion para pedir el nombre del usuario
def name_player():
    option= input("\tIngrese el nombre del jugador: ")
    P.Player(option)

#Funciones contador de las partidas ganas y perdidas  
def wins_game(player_dict):
    wins=0
    wins +=1
    player_dict.update({"wins": wins})
    A.agregar_wins(wins)

def loses_game(player_dict):
    loses=0
    loses +=1
    player_dict.update({"loses": loses})
    A.agregar_loses(loses)

#Funciones relacionadas al estado del jugador
def player_in_game():
    print("El jugador sigue en juego")

def player_loses(player_dict):
    print("El jugador ha perdido")
    loses_game(player_dict)

def player_wins(player_dict):
    print("El jugador ha ganado")
    wins_game(player_dict)

#Funciones relacionadas al estado del juego
def in_game():
    print("Sigue en juego 🂸...")

def game_over():
    print("El juego ha acabado")

#Funciones relacionadas a pedir mas o quedarse
def hit_stand(deck,hand):
    while True:
        opcion= input("\nDesea pedir más o se queda? Ingrese 'p' para pedir o 'q' para quedarse: \n" )
        if opcion[0].lower()=='p':
            hand= H.Hand()
            deck= D.Deck()
            hand.add_card(deck.deal())
        elif opcion[0].lower()=='q':
            print('El jugador se queda, Dealer jugando')
            playing=False
        else:
            print('Error, seleccione una opcion valida')
            continue
        break