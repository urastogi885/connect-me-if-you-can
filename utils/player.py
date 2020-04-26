from random import randint
from utils.game import Game
from utils.constants import PLAYER, GAME_ROBOT


class QAgent:
    def __init__(self, alpha, gamma):
        self.discount_factor = gamma
        self.learning_rate = alpha

    def load_memory(self):
        pass

    def save_memory(self):

    def get_optimal_move(self, cell_location):
        pass

    def calc_q_value(self, board, move):
        pass

    def train_with_random_agent(self, iterations):
        for _ in range(iterations):
            game = Game()
            first_player = randint(PLAYER, GAME_ROBOT)
            game_over = False
            while not game_over:
                open_cells = game.get_valid_locations()

        pass
