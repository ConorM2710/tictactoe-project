import random


# Data Model


class TicTacToe:
    """
    Represents the Tic Tac Toe game.
    """
    def __init__(self):
        """
        Occupies the game board using question marks
        """
        self.board = ['?' for i in range(9)]

    
