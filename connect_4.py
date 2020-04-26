from utils.game_gui import GameGUI


if __name__ == '__main__':
    # Initialize GUI screen and draw the game board on it
    gui = GameGUI()
    gui.draw_board()
    # Initialize game-over parameter with False to start game
    game_over = False
    # Start with the first player
    player = 0
    # Play until somebody wins
    while not game_over:
        # Keep checking for events inside the game
        game_over, player = gui.check_event(game_over, player)
