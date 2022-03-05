class Card(object):


    def __init__(self, suit=-1, value=-1):
        """Instantiates a Card object by `suit` and `value`. 
        
        The 'empty space' card is represented by passing `-1` to both `suit` and `value`

        Args:
            suit (int): The suit of the card, where 1=clubs, 2=diamonds, 3=hearts, 4=spades
            value (int): The value of the card, where 1=Ace, 11=Jack, 12=Queen, 13=King
        """
        self.value = value
        self.suit = suit
        self.set_name()
        
        # Set value and suit attributes if name is generated correctly
        # (otherwise an error is raised)


    def set_name(self):
        """Method to set the name of the card. The 'empty space' is represented by `suit=-1`, `value=-1`

        Raises:
            ValueError: if one of the values passed into `__init__()` is out of range
        """
        # Check if card is the dummy card
        if self.value == self.suit == -1:
            self.name = "   "
            return
        
        # Set the value of the card
        if self.value == 1:
            self.name = "A "
        elif self.value in range(2, 10):
            self.name = str(self.value) + " "
        elif self.value == 10:
            self.name = "10"
        elif self.value == 11:
            self.name = "J "
        elif self.value == 12:
            self.name = "Q "
        elif self.value == 13:
            self.name = "K "
        else:
            # Value error if card not a suitable value (i.e. 1-13)
            raise ValueError("invalid value for card")

        # Set the suit of the card
        if self.suit == 1:
            self.name += "♧"
        elif self.suit == 2:
            self.name += "♢"
        elif self.suit == 3:
            self.name += "♡"
        elif self.suit == 4:
            self.name += "♤"
        else:
            # Value error if suit not in range (1-4)
            raise ValueError("suit must be integer between 1-4 corresponding to clubs, diamonds, hearts, spades respectively")

    def __str__(self):
        """Prints the card by name"""
        return str(self.name)

    def __repr__(self):
        return str(self.name)
    
    def __eq__(self, other):
        if isinstance(other, Card):
            return self.value == other.value
        else:
            raise TypeError("can only compare two Card objects")
        
    def __add__(self, other):
        if isinstance(other, Card):
            return self.value + other.value
        else:
            raise TypeError("can only add two Card objects")
        
    def __gt__(self, other):
        if isinstance(other, Card):
            return self.value.__gt__(other.value)
        else:
            raise TypeError("can only compare two Card objects")
        
    def __lt__(self, other):
        if isinstance(other, Card):
            return self.value.__lt__(other.value)
        else:
            raise TypeError("can only compare two Card objects")
        
    def __le__(self, other):
        if isinstance(other, Card):
            return self.value.__le__(other.value)
        else:
            raise TypeError("can only compare two Card objects")
        
    def __ge__(self, other):
        if isinstance(other, Card):
            return self.value.__ge__(other.value)
        else:
            raise TypeError("can only compare two Card objects")
        
