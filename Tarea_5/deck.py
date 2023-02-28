# Importar modulos
import card as c
import random
# Variables de juego
suits = ('\u2663', '\u2660', '\u2666', '\u2665')
ranks = (
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
)
playing = True

# Clase deck
class deck:
    def init(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(c.card(suit,rank))

    def            

