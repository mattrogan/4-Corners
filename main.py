from card import Card
from board import Board
from random import shuffle

class GameState(object):
    
    def __init__(self):
        self.setup_deck()
        self.board = Board()
    
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
        
    def print_board(self):
        return str(self.board)
        
game = GameState()
print("The board is currently..")
print(game.board)
print("Here are three cards:")
c1 = Card(3, 5) # Five of Hearts
c2 = Card(1, 4) # Four of Clubs
c3 = Card(4, 1) # Ace of Spades
c4 = Card(2, 13) # King of Diamonds
print(c1)
print(c2)
print(c3)
print(c4)
print("Placing these in the four corners")
game.board.place(1,1,c1)
game.board.place(1,4,c2)
game.board.place(4,1,c3)
game.board.place(4,4,c4)
print(game.board)