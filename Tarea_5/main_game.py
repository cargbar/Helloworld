# Importar modulos
import Card as C
import Deck as D
import Hand as H
import Player as P
import funtions_game as F
import agregar_archivo as A

playing=True
def game():
    players_names=[]
    while True:
        print("Bienvenidos al juego de blackjack 🃍 ")
        opcion= int(input("\tElija lo que desea hacer: \n\t\t1)Seleccion de usuarios\n\t\t2)Iniciar nueva partida\n\t\t3)Ver estadisticas\n\t\t4)Salir\n"))
        #elije los usuarios
        if opcion==1:
            cantidad_players=int(input("\tIndique la cantidad de jugadores 1 o 2: "))
            for i in range(cantidad_players):
                players=int(input("\t\t1)Agregar un nuevo player\n\t\t2)Seleccionar un player existente\n"))
                #crea un nuevo jugador
                if players==1:
                    name=input("\tIngrese el nombre del jugador: ")
                    players_names.append(name)
                #selecciona un jugador existente
                elif players==2:
                    print(players_names)
                    select_player=input("Escriba el nombre del jugador que desea seleccionar: ")
                else:
                   print("Error, seleccione una opcion válida") 
        #inicia una nueva partida
        elif opcion==2:
                 #reparte las cartas y crea el mazo
                 deck= D.Deck()
                 deck.shuffle()
                 #mano del player
                 #for i in range(cantidad_players):
                 player_hand= H.Hand()
                 player_hand.add_card(deck.deal())
                 player_hand.add_card(deck.deal())
                 #mano del dealer
                 dealer_hand= H.Hand()
                 dealer_hand.add_card(deck.deal())
                 dealer_hand.add_card(deck.deal())

                 #muestra las manos e indica el estado del juego
                 F.show_some(player_hand,dealer_hand)
                 print()
                 F.in_game()

                 while playing:
                     #pregunta si se quiere quedar o pedir mas
                     F.hit_stand(deck, player_hand)
                     #muestra las manos e indica el estado del juego y del jugador
                     F.show_some(player_hand,dealer_hand)
                     F.in_game()
                     F.player_in_game()
                     if player_hand.value> 21:
                         F.player_loses()
                         A.agregar_loses()
                         break
                 if player_hand.value<= 21:
                     while dealer_hand.value< 17:
                         dealer_hand.add_card(deck.deal())
                         #muestra las manos
                         F.show_all(player_hand, dealer_hand)
                         if dealer_hand.value> 21:
                                print("El dealer ha perdido")
                                F.player_wins()
                                A.agregar_wins()
                         elif dealer_hand.value > player_hand:
                             print("El dealer ha ganado")
                             F.player_loses()
                             A.agregar_loses()
                         elif dealer_hand < player_hand:
                             print("El dealer ha perdido")
                             F.player_wins()
                             A.agregar_wins()
                         else:
                             print("Ha ocurrido un empate")
                 F.game_over()

                 pass
        #muestra las estadisticas del usuario seleccionado
        elif opcion==3:
            print(f"El jugador seleccionado ha ganado {F.wins_game()} veces, y ha perdido {F.loses_game()} veces\n")
        #salir
        elif opcion==4:
            print("Gracias por jugar!🂡")
            break
        else:
            print("Error, seleccione una opcion válida")

game()