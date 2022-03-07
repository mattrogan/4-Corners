from card import Card

class Board(object):
    
    def __init__(self):
        """Constructor for 4x4 Board object"""
        self.state = [[Card(-1, -1) for _ in range(4)] for _ in range(4)]
        
    def place(self, i, j, card):
        """Places `card` at position `(i,j)` on the board.

        Args:
            i (int): row of location to place the card
            j (int): column of location to place the card
            card (Card): the card to be placed on the board

        Raises:
            TypeError: if a non-Card object is passed, or a non-integer for the position.
            ValueError: if the space `(i,j)` is already filled.
        """
        row = i - 1
        col = j - 1
        
        # Assert that card is a Card object 
        if not isinstance(card, Card):
            raise TypeError("card must be a Card object")
        
        # Assert that i/j are valid positions
        if not isinstance(i, int) or not isinstance(j, int):
            raise TypeError("position (row, col) of card must be integers")
        
        # Assert the position is free
        if self.state[row][col].value == -1:
            self.state[row][col] = card
        else:
            raise ValueError("Space already has a card placed here")
        
    def clear_board(self):
        """Clears the board for a new game
        """
        self.state = [[Card(-1, -1) for _ in range(4)] for _ in range(4)]
          
    def __str__(self):
        returnStr = ""
        for row in self.state:
            returnStr += str(row) +"\n"
        return returnStr[:-1] # Remove the last newline return
    
    def __repr__(self):
        return str(self)