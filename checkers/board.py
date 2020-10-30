import pygame
from .constants import BLACK, RED, WHITE, ROWS, COLUMNS, SQUARE_SIZE
from .piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_remaining = 12
        self.white_remaining = 12
        self.red_kings = 0
        self.white_kings = 0
        self.create_board()

    def draw_squares(self, window):
        window.fill(BLACK)
        for row in range(ROWS):
            for column in range(row % 2, COLUMNS, 2):
                pygame.draw.rect(window, RED, (row * SQUARE_SIZE, column * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])  # initializing lists of pieces for each row
            for column in range(COLUMNS):
                if column % 2 == ((row + 1) % 2):  # alternates positions based on row
                    if row < 3:
                        self.board[row].append(Piece(row, column, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, column, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, window):
        self.draw_squares(window)
        for row in range(ROWS):
            for column in range(COLUMNS):
                piece = self.board[row][column]
                if piece != 0:
                    piece.draw(window)
