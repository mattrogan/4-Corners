class Card(object):


    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.name = self.set_name()

    def set_name(self):
        if self.value == 1:
            self.name = "Ace"
        elif self.value in range(2, 11):
            self.name = str(self.value)
        elif self.value == 11:
            self.name = "Jack"
        elif self.value == 12:
            self.name = "Queen"
        elif self.value == 13:
            self.name = "King"
        else:
            raise ValueError("invalid value for card")

        self.name += " of "

        if self.suit == 1:
            self.name += "Clubs"
        elif self.suit == 2:
            self.name += "Diamonds"
        elif self.suit == 3:
            self.name += "Hearts"
        elif self.suit == 4:
            self.name += "Spades"
        else:
            raise ValueError("suit must be integer between 1-4 corresponding to clubs, diamonds, hearts, spades respectively")

    def __str__(self):
        return str(self.name)


# Ace of Spaces
c1 = Card(4, 1)
print(c1.name)

# Jack of Diamonds
c2 = Card(2, 11)
print(c2.name)