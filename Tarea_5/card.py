# Clase Carta:
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def str(self):
        return self.rank + "of" + self.suit
