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

    def show_board(self):
        """
        Displays the game board
        """
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print("--|--|--")
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print("--|--|--")
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2])


    
