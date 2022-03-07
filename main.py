from card import Card
from board import Board
from random import shuffle

class GameState(object):
    
    def __init__(self):
        self.setup_deck()
        self.board = Board()
        
    def play(self):
        # Place the initial four cards
        for i in [1, 4]:
            for j in [1, 4]:
                self.board.place(i, j, self.deck.pop(0))
        
        still_going = True
        
        print("The board starts like this:")        
        self.print_board()
        
        while still_going:
            print("Enter row and column for next card")
            row = int(input("Row: "))        
            col = int(input("Column: "))
    
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
        return print(game.board)
        
game = GameState()
game.play()