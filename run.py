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

    def user_input(self, move):
        """
        Prompts the user to enter an input and updates the board
        """
        while True:
            try:
                space = int(input(f"Enter a number between 1 and 9 to place your '{move}' mark"))
                if space < 1 or space > 9:
                    raise ValueError("Invalid input. Please enter a number between 1 and 9.")
                space -= 1
                if self.board[space] != "?":
                    raise ValueError("That space is already taken. Please choose another space")
                self.board[space] = move
                break
            except ValueError as e:
                print(e) 

    def check_winner(self):
        """
        Checks the three functions to determine the winner
        """

        # Checks Columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[
                    i+6] and self.board[i] != "?":
                return self.board

        # Checks Rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[
                    i+2] and self.board[i] != "?":
                return self.board

        # Checks Diagonals
        if self.board[0] == self.board[4] == self.board[
                    8] and self.board[0] != "?":
            return self.board
        elif self.board[2] == self.board[4] == self.board[
                    6] and self.board[2] != "?":
            return self.board[2]

        # Draw
        if "?" not in self.board:
            return "draw"

    def play_game(self):
        """
        Runs the tic tac toe game
        """
        print("Welcome to Tic Tac Toe!\n")
        self.show_board()
        while True:
            self.user_input("X")
            self.show_board()
            winner = self.check_winner()
            if winner:
                break
            self.user_input("O")
            self.show_board()
            winner = self.check_winner()
            if winner:
                break

        if winner == "draw":
            print("Oops there is no more spaces left, its a draw!")
        else:
            print(f"The player {winner} has won the game!\n")