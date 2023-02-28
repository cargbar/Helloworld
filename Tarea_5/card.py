# Clase Carta:
class card:
    def init(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def str(self):
        return self.rank + "of" + self.suit
