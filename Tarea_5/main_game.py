'''
Funcion principal que corre el juego. Se compone de otras funciones importadas por medio de modulos
'''
# Importar modulos
import Hand as H
import Game as G
import funtions_game as F
import agregar_archivo as A

playing=True
def game():
    player=""
    cantidad_players=0 
    while True:
        print("Bienvenidos al juego de blackjack 🃍 ")
        opcion= int(input("\tElija lo que desea hacer: \n\t\t1)Seleccion de usuarios\n\t\t2)Iniciar nueva partida\n\t\t3)Ver estadisticas\n\t\t4)Salir\n"))
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

                 while playing:
                     #pregunta si se quiere quedar o pedir mas
                     F.hit_stand(juego.playerhands, juego.deck)
                     #muestra las manos e indica el estado del juego y del jugador
                     juego.print_players_hands()
                     print()
                     F.in_game()
                     print()
                     juego.player_in_game()
                     F.game_scenarios(player,juego.playerhands, juego.deck)
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