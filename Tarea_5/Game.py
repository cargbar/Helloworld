'''
La clase Game contiene la logica de crear el mazo, repartir las cartas a cada jugador, y mostrar las manos de cada jugador.
Tambien contiene funciones que muestran el estado del jugador
'''
import deck as D
import Hand as H
import agregar_archivo as A

class Game:
    def __init__(self, playernames):
        #Reparte las cartas y crea el mazo
        deck= D.Deck()
        deck.shuffle()
        manos_players=[]

        #Mano del dealer
        dealer_hand= H.Hand("Dealer")
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        #Mano del player
        for player in playernames:
            player_hand= H.Hand(player)
            player_hand.add_card(deck.deal())
            player_hand.add_card(deck.deal())
            manos_players.append(player_hand)
        
        self.deck=deck
        self.dealerhand=dealer_hand
        self.playerhands= manos_players
    
    #Muestra las manos de cada jugador
    def print_players_hands(self):
        self.dealerhand.show_hand(True)
        for hand in self.playerhands:
            hand.show_hand()

    #Funciones que indican el estado del jugador
    def player_in_game(self):
        for hand in self.playerhands:
            print("El jugador sigue en juego")

    def player_loses(self,playername, result):
        for hand in self.playerhands:
            print("El jugador ha perdido")
        A.add_player_stats(playername,"Perdió")

    def player_wins(self, playername, result):
         for hand in self.playerhands:
            print(f"El jugador ha ganado")
         A.add_player_stats(playername, "Ganó")