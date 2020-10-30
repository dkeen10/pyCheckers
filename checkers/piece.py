import pygame
from .constants import RED, WHITE, SQUARE_SIZE


class Piece:
    PADDING = 8
    BORDER = 2

    def __init__(self, row, column, colour):
        up = -1
        down = 1

        self.row = row
        self.column = column
        self.colour = colour
        self.king = False
        self.selected = False
        self.x_pos = 0
        self.y_pos = 0
        self.calc_pos()

        if self.colour == RED:
            self.direction = up
        else:
            self.direction = down

    def calc_pos(self):
        self.x_pos = SQUARE_SIZE * self.column + SQUARE_SIZE // 2
        self.y_pos = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, window):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(window, self.colour, (self.x_pos, self.y_pos), radius)
        pygame.draw.circle(window, self.colour, (self.x_pos, self.y_pos), radius + self.BORDER)

    def __repr__(self):
        """Returns a string representation of this piece."""
        return str(self.colour)
