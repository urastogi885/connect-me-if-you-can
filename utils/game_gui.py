import pygame
from sys import exit
from utils.game import Game
from utils.constants import *


class Connect4GUI:
    def __init__(self):
        """
        Initialize the GUI
        """
        # Initialize the game
        self.game = Game()
        # Initialize the GUI screen
        pygame.init()
        self.screen = pygame.display.set_mode(GUI_SIZE)
        pygame.display.update()
        # Define font to print winner
        self.font = pygame.font.SysFont('monospace', 75)

    def draw_board(self):
        """
        Draw the empty configuration of the game
        :return: nothing
        """
        # Draw rectangle to represent the board area where coins go in
        pygame.draw.rect(self.screen, BLUE, (0, CELL_SIZE, GUI_SIZE[0], GUI_SIZE[1] - CELL_SIZE))
        # Draw circles to represent dots in the game
        for i in range(BOARD_SIZE[0]):
            for j in range(BOARD_SIZE[1]):
                center = (j * CELL_SIZE + (CELL_SIZE // 2)), ((i + 1) * CELL_SIZE + (CELL_SIZE // 2))
                pygame.draw.circle(self.screen, BLACK, center, RADIUS)
        # Update GUI
        pygame.display.update()

    def check_event(self, player):
        """
        Function to check for events occurring inside the GUI screen
        :return: nothing
        """
        game_status = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(self.screen, BLACK, (0, 0, GUI_SIZE[1], CELL_SIZE))
                col_index = int(event.pos[0] / CELL_SIZE)
                center = ((col_index * CELL_SIZE) + (CELL_SIZE // 2)), (CELL_SIZE // 2)
                if player:
                    pygame.draw.circle(self.screen, YELLOW, center, RADIUS)
                else:
                    pygame.draw.circle(self.screen, RED, center, RADIUS)
            elif event.type == pygame.MOUSEBUTTONUP:
                pygame.draw.rect(self.screen, BLACK, (0, 0, GUI_SIZE[1], CELL_SIZE))
                col_index = int(event.pos[0] / CELL_SIZE)
                row_index = self.game.get_open_row(col_index)
                center = ((col_index * CELL_SIZE) + (CELL_SIZE // 2)), (CELL_SIZE // 2)
                if row_index != -1:
                    center = (((col_index * CELL_SIZE) + (CELL_SIZE // 2)),
                              (((BOARD_SIZE[0] - row_index) * CELL_SIZE) + (CELL_SIZE // 2)))
                    self.game.add_coin(row_index, col_index, player)
                if player:
                    pygame.draw.circle(self.screen, YELLOW, center, RADIUS)
                else:
                    pygame.draw.circle(self.screen, RED, center, RADIUS)
                if self.game.is_winning_move(row_index, col_index, player):
                    if player:
                        label = self.font.render('Player ' + str(player + 1) + ' Wins!', True, YELLOW)
                    else:
                        label = self.font.render('Player ' + str(player + 1) + ' Wins!', True, RED)
                    self.screen.blit(label, (40, 10))
                    game_status = True
                if row_index != -1:
                    player = (player + 1) % 2
        # Update GUI
        pygame.display.update()
        if game_status:
            pygame.time.wait(5000)
        return player, game_status
