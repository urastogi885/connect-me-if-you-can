import numpy as np
from utils.constants import BOARD_SIZE


class Game:
    def __init__(self):
        """
        Initialize the game class with an empty board
        """
        self.board = np.zeros(BOARD_SIZE, dtype=np.int8)

    def add_player_token(self, row, col, player):
        """
        Method to fill a position with player's token
        :param row: row in the board where the token needs to be placed
        :param col: column in the board where the token needs to be placed
        :param player: player whose token needs to be added in the board
        :return: nothing
        """
        # Add token of the player in the given row-column
        self.board[row][col] = player + 1

    def get_open_row(self, col):
        """
        Method to get the lower-most empty row on the board in a column
        :param col: column on the board to find the empty row
        :return: index of the lower-most row in the given column
        """
        # Iterate through the rows of the given column
        for row in range(BOARD_SIZE[0]):
            if self.board[row][col] == 0:
                # Return the index of the lower-most empty row
                return row
        # Return -1 if none of the rows in the given column on the board is empty
        return -1

    def is_winning_move(self, row, col, player):
        """
        Method to check is the last move by a player wins the game
        :param row: index of the row where the last token of the player was placed
        :param col: index of the column where the last token of the player was placed
        :param player: player whose token was placed last
        :return: boolean value whether the last move was a winning move
        """
        return (self.check_horizontal_win(row, col, player) or self.check_vertical_win(row, col, player) or
                self.check_diagonal_win(row, col, player))

    def check_horizontal_win(self, row, col, player):
        """
        Method to check for winning move along the columns
        :param row: index of the row where the last token of the player was placed
        :param col: index of the column where the last token of the player was placed
        :param player: player whose token was placed last
        :return: boolean value whether the last move was a winning move
        """
        # If all pieces lie ahead of the last dropped piece
        try:
            if (self.board[row][col + 1] == player + 1 and self.board[row][col + 2] == player + 1 and
                    self.board[row][col + 3] == player + 1):
                return True
        except IndexError:
            pass
        # If 2 pieces lie ahead and 1 piece lies behind the last dropped piece
        try:
            if (self.board[row][col + 1] == player + 1 and self.board[row][col + 2] == player + 1 and
                    self.board[row][col - 1] == player + 1):
                return True
        except IndexError:
            pass
        # If 1 piece lies ahead and 2 pieces lie behind the last dropped piece
        try:
            if (self.board[row][col + 1] == player + 1 and self.board[row][col - 2] == player + 1 and
                    self.board[row][col - 1] == player + 1):
                return True
        except IndexError:
            pass
        # If all pieces lie behind the last dropped piece
        try:
            if (self.board[row][col - 1] == player + 1 and self.board[row][col - 2] == player + 1 and
                    self.board[row][col - 3] == player + 1):
                return True
        except IndexError:
            pass
        return False

    def check_vertical_win(self, row, col, player):
        """
        Method to check for winning move along the rows
        :param row: index of the row where the last token of the player was placed
        :param col: index of the column where the last token of the player was placed
        :param player: player whose token was placed last
        :return: boolean value whether the last move was a winning move
        """
        if row <= BOARD_SIZE[0] // 2:
            if (self.board[row - 1][col] == player + 1 and self.board[row - 2][col] == player + 1 and
                    self.board[row - 3][col] == player + 1):
                return True
        return False

    def check_diagonal_win(self, row, col, player):
        """
        Method to check for winning move along the diagonals
        :param row: index of the row where the last token of the player was placed
        :param col: index of the column where the last token of the player was placed
        :param player: player whose token was placed last
        :return: boolean value whether the last move was a winning move
        """
        # Checks for the positively-sloped diagonal wins
        # If all pieces lie ahead of the last dropped piece
        try:
            if (self.board[row + 1][col + 1] == player + 1 and self.board[row + 2][col + 2] == player + 1 and
                    self.board[row + 3][col + 3] == player + 1):
                return True
        except IndexError:
            pass
        # If 2 pieces lie ahead and 1 piece lies behind the last dropped piece
        try:
            if (self.board[row + 1][col + 1] == player + 1 and self.board[row + 2][col + 2] == player + 1 and
                    self.board[row - 1][col - 1] == player + 1):
                return True
        except IndexError:
            pass
        # If 1 piece lies ahead and 2 pieces lie behind the last dropped piece
        try:
            if (self.board[row - 1][col - 1] == player + 1 and self.board[row - 2][col - 2] == player + 1 and
                    self.board[row + 1][col + 1] == player + 1):
                return True
        except IndexError:
            pass
        # If all pieces lie behind the last dropped piece
        try:
            if (self.board[row - 1][col - 1] == player + 1 and self.board[row - 2][col - 2] == player + 1 and
                    self.board[row - 3][col - 3] == player + 1):
                return True
        except IndexError:
            pass
        # Checks for the negatively-sloped diagonal wins
        # If all pieces lie behind the last dropped piece
        try:
            if (self.board[row - 1][col + 1] == player + 1 and self.board[row - 2][col + 2] == player + 1 and
                    self.board[row - 3][col + 3] == player + 1):
                return True
        except IndexError:
            pass
        # If 1 piece lies ahead and 2 pieces lie behind the last dropped piece
        try:
            if (self.board[row - 1][col + 1] == player + 1 and self.board[row - 2][col + 2] == player + 1 and
                    self.board[row + 1][col - 1] == player + 1):
                return True
        except IndexError:
            pass
        # If 2 pieces lie ahead and 1 piece lies behind the last dropped piece
        try:
            if (self.board[row + 1][col - 1] == player + 1 and self.board[row + 2][col - 2] == player + 1 and
                    self.board[row - 1][col + 1] == player + 1):
                return True
        except IndexError:
            pass
        # If all pieces lie ahead of the last dropped piece
        try:
            if (self.board[row + 1][col - 1] == player + 1 and self.board[row + 2][col - 2] == player + 1 and
                    self.board[row + 3][col - 3] == player + 1):
                return True
        except IndexError:
            pass
        return False
