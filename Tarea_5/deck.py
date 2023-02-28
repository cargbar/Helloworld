# Importar modulos
import random
import Card as c

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
    def init(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(c.card(suit, rank))

    def str(self):
        deck_comp = ""
        for c.card in self.deck:
            deck_comp += "\n" + c.card.str()
            return "the deck has" + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card
