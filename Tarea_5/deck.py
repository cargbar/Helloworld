# Importar modulos
import random
import Card as C

# Variables de juego
suits = ("\u2663", "\u2660", "\u2666", "\u2665")
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
                self.deck.append(C.Card(suit,rank))

    def __str__(self):
        deck_comp = ""
        for C.Card in self.deck:
            deck_comp += "\n" + C.Card.str()
            return "the deck has" + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

