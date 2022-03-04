from card import Card
from random import shuffle

def GameState(object):
    
    def __init__(self):
        self.setup_deck()
    
    def setup_deck(self):
        """Method to set up the deck of cards
        """
        # Create empty deck object
        self.deck = []
        
        for i in range(4):
            # Iterate 4 times for each suit
            suit = i + 1

            for j in range(13):
                # Iterate 13 times for each card in the suit
                value = j + 1

                self.deck.append(Card(suit, value))

        # Randomise the order of the deck
        shuffle(self.deck)