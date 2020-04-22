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
        if col <= BOARD_SIZE[1] // 2:
            if (self.board[row][col + 1] == player + 1 and self.board[row][col + 2] == player + 1 and
                    self.board[row][col + 3] == player + 1):
                return True
        else:
            if (self.board[row][col - 1] == player + 1 and self.board[row][col - 2] == player + 1 and
                    self.board[row][col - 3] == player + 1):
                return True
        return False

    def check_vertical_win(self, row, col, player):
        if row <= BOARD_SIZE[0] // 2:
            if (self.board[row - 1][col] == player + 1 and self.board[row - 2][col] == player + 1 and
                    self.board[row - 3][col] == player + 1):
                return True
        return False

    def check_diagonal_win(self, row, col, player):
        if row < BOARD_SIZE[0] // 2 and col <= (BOARD_SIZE[1] // 2) + 1:
            if (self.board[row + 1][col + 1] == player + 1 and self.board[row + 2][col + 2] == player + 1 and
                    self.board[row + 3][col + 3] == player + 1):
                return True
        elif BOARD_SIZE[0] // 2 <= row and col <= (BOARD_SIZE[1] // 2) + 1:
            if (self.board[row - 1][col + 1] == player + 1 and self.board[row - 2][col + 2] == player + 1 and
                    self.board[row - 3][col + 3] == player + 1):
                return True
        if BOARD_SIZE[0] // 2 <= row and BOARD_SIZE[1] // 2 <= col:
            if (self.board[row - 1][col - 1] == player + 1 and self.board[row - 2][col - 2] == player + 1 and
                    self.board[row - 3][col - 3] == player + 1):
                return True
        elif row < BOARD_SIZE[0] // 2 and BOARD_SIZE[1] // 2 <= col:
            if (self.board[row + 1][col - 1] == player + 1 and self.board[row + 2][col - 2] == player + 1 and
                    self.board[row + 3][col - 3] == player + 1):
                return True
        return False
