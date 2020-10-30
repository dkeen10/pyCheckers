import pygame
from .constants import RED, WHITE, SQUARE_SIZE, CROWN


class Piece:
    """
    Represents a Checkers Piece.
    """
    PADDING = 8
    BORDER = 2

    def __init__(self, row, column, colour):
        """
        Initialize a new Piece Object.

        :param row: an int
        :param column: an int
        :param colour: an rgb colour
        """
        self.row = row
        self.column = column
        self.colour = colour
        self.king = False
        self.x_pos = 0
        self.y_pos = 0
        self.calc_pos()

    def calc_pos(self):
        """
        Calculate the position of the Piece.
        """
        self.x_pos = SQUARE_SIZE * self.column + SQUARE_SIZE // 2
        self.y_pos = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        """
        Set the piece as a king.
        """
        self.king = True

    def draw(self, window):
        """
        Draw the piece on the board.

        :param window: the pygame window
        """
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(window, self.colour, (self.x_pos, self.y_pos), radius)
        pygame.draw.circle(window, self.colour, (self.x_pos, self.y_pos), radius + self.BORDER)
        if self.king:
            window.blit(CROWN, (self.x_pos - CROWN.get_width() // 2, self.y_pos - CROWN.get_height() // 2))

    def move(self, row, column):
        """
        Move the piece on the board.

        :param row: an int
        :param column: an int
        """
        self.row = row
        self.column = column
        self.calc_pos()

    def __repr__(self):
        """
        Returns a string representation of this piece.
        """
        return str(self.colour)
