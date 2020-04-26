# Row-by-column representation of the board
BOARD_SIZE = 6, 7
# Define size of each cell in the GUI of the game
CELL_SIZE = 100
# Define radius of dot
RADIUS = (CELL_SIZE // 2) - 5
# Define size of GUI screen
GUI_SIZE = (BOARD_SIZE[0] + 1) * CELL_SIZE, (BOARD_SIZE[1]) * CELL_SIZE
# Define various colors used on the GUI of the game
RED = 255, 0, 0
BLUE = 0, 0, 255
BLACK = 0, 0, 0
WHITE = 255, 255, 255
YELLOW = 255, 255, 0
# Define various players in the Game
HUMAN_PLAYER = 0
Q_ROBOT = 1
RANDOM_ROBOT = 2
# Define various rewards
REWARD_WIN = 1
REWARD_LOSS = -1
REWARD_DRAW = 0.5
REWARD_NOTHING = 0
