from utils.game_gui import *


if __name__ == '__main__':
    gui = Connect4GUI()
    gui.draw_board()
    game_over = False
    player = 0
    while not game_over:
        player, game_over = gui.check_event(player)
