import random
import json
from numpy import ravel_multi_index
from copy import deepcopy
from utils.constants import *


class Player:
    """
    A class to represent various types of players in the game
    By default, it represents a human player
    """
    def __init__(self, token=HUMAN_PLAYER):
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
    def __init__(self, token=Q_ROBOT, alpha=0.9, gamma=0.75, epsilon=0.9, mem_location=MEM_LOCATION):
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
        self.load_memory(mem_location)

    def load_memory(self, file_location=MEM_LOCATION):
        with open(file_location, 'r') as memory:
            self.q_value = json.load(memory)
        memory.close()

    def save_memory(self, file_location=MEM_LOCATION):
        with open(file_location, 'w+') as memory:
            json.dump(self.q_value, memory, indent=2)
        memory.close()

    @staticmethod
    def get_key(state):
        return str(tuple(map(tuple, state)))

    def get_optimal_move(self, current_state, moves):
        # Allow the robot to explore random moves
        if random.random() < self.exploration_chance:
            return random.choice(moves)
        # Get maximum Q-value
        max_q_value, q_values = self.get_max_q_value(current_state, moves)
        # Check if there are more than 1 instances of maximum Q-value
        if q_values.count(max_q_value) > 1:
            # Choose a random instance among the various instances of maximum Q-value
            max_options = [i for i in range(len(moves)) if q_values[i] == max_q_value]
            selected_option = random.choice(max_options)
            return moves[selected_option]
        # Return move with the max Q-value
        return moves[q_values.index(max_q_value)]

    def get_q_value(self, state, move):
        """
        Method to retrieve Q-value based on the state-action pair
        :param state: State of the game whose Q-value needs to be extracted
        :param move: Action done on the state
        :return: Q-value of the given state-action pair
        """
        # Convert move into an index
        move = str(ravel_multi_index(move, dims=BOARD_SIZE))
        # Convert state-action pair into a string
        key = self.get_key(state)
        # Check if the state-action pair exists
        if self.q_value.get(key) is None:
            self.q_value[key] = {move: 1.0}
        else:
            if self.q_value[key].get(move) is None:
                self.q_value[key][move] = 1.0
        return self.q_value[key][move]

    def calc_q_value(self, reward, prev_q_value, max_q_value):
        """
        Method to calculate Q-value
        :param reward: Reward based on the current state of the board
        :param prev_q_value: Q-value of the previous state of the board
        :param max_q_value: Maximum Q-value out of the current state of the board and available moves
        :return: Q-value of the given state
        """
        # Apply the Bellman's equation
        return prev_q_value + self.learning_rate * (reward + (self.discount_factor * max_q_value) - prev_q_value)

    def get_max_q_value(self, state, moves):
        """
        Method to get the maximum Q-value of the current state of the board
        :param next_states: a list of possible state of the board w.r.t each of the possible moves
        :param moves: a list of possible moves on the board
        :return: maximum Q-value of the current state of the board and list of all Q-values
        """
        # Generate a list of Q-values for each state-action pair
        q_values = [self.get_q_value(state, move) for move in moves]
        return max(q_values), q_values

    def train(self, valid_moves, reward, player, game):
        """
        Method to train the robot of the game using Q-Learning
        :param valid_moves: a list of possible moves on the board
        :param reward: reward based on the current status of the board
        :param player: ID of the player to train
        :param game: an instance of the Game class
        :return: nothing
        """
        for move in valid_moves:
            current_state = deepcopy(game.current_state)
            # Get the Q-value of the previous state of the game
            prev_q_value = self.get_q_value(current_state, move)
            next_state = deepcopy(game.current_state)
            next_state[move[0]][move[1]] = player + 1
            next_moves = game.get_valid_locations(next_state)
            if len(next_moves):
                # Get the maximum Q-value of the current state of the game
                max_q_value, _ = self.get_max_q_value(next_state, next_moves)
                # Update Q-value of the state-action pair
                move = str(ravel_multi_index(move, dims=BOARD_SIZE))
                self.q_value[self.get_key(current_state)][move] = self.calc_q_value(reward, prev_q_value, max_q_value)


class RandomPlayer(Player):
    """
    A class that represents a player that picks moves randomly
    """

    def __init__(self, token=RANDOM_ROBOT):
        """
        Initialize the human player with its token
        :param token: integer that represents the player on the board
        """
        Player.__init__(self, token)

    def make_move(self, valid_moves):
        """
        Method to make a move on the board
        :return: a tuple containing location of the token to be placed
        """
        return random.choice(valid_moves)


class MinMaxPlayer(Player):
    """
    A class that represents a player trained using the MinMax algorithm
    """
    def __init__(self, token=MINMAX_ROBOT):
        """
        Initialize the min-max player with its token
        :param token: integer that represents the player on the board
        """
        self.token = token
