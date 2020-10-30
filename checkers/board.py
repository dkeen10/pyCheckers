import pygame
from .constants import BLACK, RED, ROWS, SQUARE_SIZE


class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_remaining = 12
        self.white_remaining = 12
        self.red_kings = 0
        self.white_kings = 0

    def draw_squares(self, window):
        window.fill(BLACK)
        for row in range(ROWS):
            for column in range(row % 2, ROWS, 2):
                pygame.draw.rect(window, RED, (row * SQUARE_SIZE, column * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
