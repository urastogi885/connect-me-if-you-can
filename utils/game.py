import numpy as np
from utils.constants import BOARD_SIZE


class Game:
    def __init__(self):
        self.board = np.zeros(BOARD_SIZE, dtype=np.int8)

    def add_coin(self, row, col, player):
        self.board[row][col] = player + 1

    def get_open_row(self, col):
        for row in range(BOARD_SIZE[0]):
            if self.board[row][col] == 0:
                return row
        return -1

    def is_winning_move(self, row, col, player):
        return (self.check_horizontal_win(row, col, player) or self.check_vertical_win(row, col, player) or
                self.check_diagonal_win(row, col, player))

    def check_horizontal_win(self, row, col, player):
        try:
            if (self.board[row][col + 1] == player + 1 and self.board[row][col + 2] == player + 1 and
                    self.board[row][col + 3] == player + 1):
                return True
        except IndexError:
            pass
        try:
            if (self.board[row][col + 1] == player + 1 and self.board[row][col + 2] == player + 1 and
                    self.board[row][col - 1] == player + 1):
                return True
        except IndexError:
            pass
        try:
            if (self.board[row][col + 1] == player + 1 and self.board[row][col - 2] == player + 1 and
                    self.board[row][col - 1] == player + 1):
                return True
        except IndexError:
            pass
        try:
            if (self.board[row][col - 1] == player + 1 and self.board[row][col - 2] == player + 1 and
                    self.board[row][col - 3] == player + 1):
                return True
        except IndexError:
            pass
        return False

    def check_vertical_win(self, row, col, player):
        if row <= BOARD_SIZE[0] // 2:
            if (self.board[row - 1][col] == player + 1 and self.board[row - 2][col] == player + 1 and
                    self.board[row - 3][col] == player + 1):
                return True
        return False

    def check_diagonal_win(self, row, col, player):
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
