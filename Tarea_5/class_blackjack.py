# Importar modulos
import random

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
values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11,
}
playing = True


# Clase Carta:
class card:
    def init(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def str(self):
        return self.rank + "of" + self.suit


# Clase Deck:
class deck:
    def init(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(card(suit, rank))

    def str(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += "\n" + card.str()
        return "The deck has" + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


# Clase hand
class hand:
    def init(self):
        self.cards = []
        self.value = 0
        self.ace = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces -= 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
