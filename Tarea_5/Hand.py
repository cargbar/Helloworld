'''
Clase Hand, donde se encuentran los valores de las cartas. Tienen funciones utiles como añadir cartas a la mano de un jugador, y mostrarlas
'''
# Valores cartas
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


# Clase hand
class Hand:
    def __init__(self, playername):
        self.playername= playername
        self.cards = []
        self.value = 0

    #Agrega cartas u la mano del jugador
    def add_card(self, card):
        self.cards.append(card.str())
        self.value += values[card.rank]

    #Muestra la mano de los jugadores y del dealer
    def show_hand(self, isdealer=False):
        print(f"\tLa mano del jugador {self.playername} es: ")
        for i in range (0, len(self.cards)):
            if isdealer and i==0:
                print("⋆")
            else:
                print(self.cards[i])
        show_value= "⋆" if isdealer else self.value
        print(f"\tEl valor de la mano es de: {show_value}")

