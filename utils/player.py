from utils.constants import HUMAN_PLAYER, Q_ROBOT, RANDOM_ROBOT


class Player:
    """
    A class to represent various types of players in the game
    By default, it represents a human player
    """
    def __init__(self, token=HUMAN_PLAYER + 1):
        """
        Initialize player with its token
        :param token: integer that represents the player on the board
        """
        self.token = token

    def make_move(self):
        """
        Method to make a move on the board
        :return: nothing
        """
        pass


class QPlayer(Player):
    """
    A class that represents a Q-learning based AI player
    """
    def __init__(self, token=Q_ROBOT + 1, alpha=0.3, gamma=0.9, epsilon=0.2):
        """
        Initialize the player with its token, learning rate, discount factor, and exploration chance
        :param token: integer that represents the player on the board
        :param alpha: learning rate of the AI player; value between 0-1
        :param gamma: discount factor for future rewards; value between 0-1
        :param epsilon: probability of random exploration; value between 0-1
        """
        Player.__init__(self, token)
        self.discount_factor = gamma
        self.learning_rate = alpha
        self.exploration_chance = epsilon
        self.q_value = {}

    def load_memory(self):
        pass

    def save_memory(self):
        pass

    def get_optimal_move(self, cell_location):
        pass

    def get_q_value(self, board, move):
        pass

    def calc_q_value(self):
        pass

    def train(self, iterations):
        pass


class RandomPlayer(Player):
    """
    A class that represents a player that picks moves randomly
    """

    def __init__(self, token=RANDOM_ROBOT + 1):
        """
        Initialize the human player with its token
        :param token: integer that represents the player on the board
        """
        Player.__init__(self, token)
