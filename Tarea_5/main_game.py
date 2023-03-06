'''
Funcion principal que corre el juego. Se compone de otras funciones importadas por medio de modulos
'''
# Importar modulos
import Hand as H
import Game as G
import funtions_game as F
import agregar_archivo as A


def game():
    player=""
    cantidad_players=0 
    while True:
        print("Bienvenidos al juego de blackjack 🃍 ")
        opcion = int(input("\tElija lo que desea hacer: \n\t\t1)Seleccion de usuarios\n\t\t2)Iniciar nueva partida\n\t\t3)Ver estadisticas\n\t\t4)Salir\n"))
        
        #elije los usuarios
        if opcion==1:
            cantidad_players=int(input("\tIndique la cantidad de jugadores 1 o 2: "))
            for i in range(cantidad_players):
                player= F.handle_player_select()

        #inicia una nueva partida
        elif opcion==2:
                 #llama a la clase que reparte las manos a los jugadores
                 juego= G.Game([player])
                 #muestra las manos e indica el estado del juego
                 juego.print_players_hands()
                 print()
                 F.in_game()
                 
                 playing = True
        
                 while playing:
                       
                       for hand in juego.playerhands: 
                        #pregunta si se quiere quedar o pedir mas
                        playing = F.hit_stand(hand, juego.deck)
                        #muestra las manos e indica el estado del juego y del jugador
                        juego.print_players_hands()
                        print()
                        F.in_game()
                        print()
                        juego.player_in_game()
                        #si la mano del jugador es mayor a 21, llama a funcion player_loses() y se sale del loop
                        if hand.value >21:
                            juego.player_loses(player, "Perdio")
                            break
                 #Si el jugador no perdió, se juego con el Dealer
                 if juego.dealerhand.value <=21:
                    print(
                        "EL DEALER ESTA JUGANDO"
                    )
                    while juego.dealerhand.value <17:
                        F.hit(juego.dealerhand, juego.deck)
                        #muestra las manos
                        # H.Hand('TEST').show_hand(False)
                        juego.dealerhand.show_hand(True)
                        #Escenarios de juego respecto al Dealer
                        if juego.dealerhand.value >21:
                            print("El dealer ha perdido")
                            juego.player_wins(player, "Gano")
                        for hand in juego.playerhands: 
                            if juego.dealerhand.value > hand.value or (juego.dealerhand.value + 1 > hand.value ):
                                print("El dealer ha ganado")
                                juego.player_loses(player, "Perdio")
                        for hand in juego.playerhands:
                            if juego.dealerhand.value < hand.value:
                                print("El dealer ha perdido")
                                juego.player_wins(player, "Gano")
                        # for hand in juego.playerhands:
                        #     if juego.dealerhand.value +1 > hand.value:
                        #         print("El dealer ha ganado")
                        #         juego.player_loses(player, "Perdio")
                 F.game_over()
        
        #muestra las estadisticas del usuario seleccionado
        elif opcion==3:
            F.show_stats()
        
        #salir
        elif opcion==4:
            print("Gracias por jugar!🂡")
            break
        else:
            print("Error, seleccione una opcion válida")

game()