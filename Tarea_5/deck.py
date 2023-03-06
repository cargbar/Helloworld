'''
En la clase Deck se encuentran los valores de los palos y los rangos de las cartas. Esta clase crea el mazo del juego, mezclando y repartiendo las cartas entre los jugadores.
'''

# Importar modulos
import random
import card as C

# Variables de juego
suits = ("\u2764", "\u2666", "\u2660", "\u2618")
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


# Clase deck
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(C.Card(suit, rank))

    def __str__(self):
        deck_comp = ""
        for C.Card in self.deck:
            deck_comp += "\n" + C.Card.str()
            return "the deck has" + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        # print('print deck:', self.deck)
        # print('print deck: \n ',[card.str() for card in self.deck])
        # print(len(self.deck))
        single_card = self.deck.pop()
        return single_card
