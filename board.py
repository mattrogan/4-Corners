from card import Card

class Board(object):
    
    def __init__(self):
        
        self.state = [[Card(-1, -1) for _ in range(4)] for _ in range(4)]
        
    def place(self, i, j, card):
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
            print(f"Card placed at ({i},{j})")
            self.state[row][col] = card
        else:
            print("You cannot place this card here.")
        

          
    def __str__(self):
        returnStr = ""
        for row in self.state:
            returnStr += str(row) +"\n"
        return returnStr[:-1] # Remove the last newline return