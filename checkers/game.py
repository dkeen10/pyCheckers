import pygame
from .board import Board
from .constants import RED, WHITE, BLUE, SQUARE_SIZE


class Game:
    def __init__(self, window):
        self._init()
        self.window = window

    def update(self):
        self.board.draw(self.window)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    def reset(self):
        self._init()

    def select(self, row, column):
        if self.selected:
            result = self._move(row, column)
            if not result:
                self.selected = None
                self.select(row, column)
        piece = self.board.get_piece(row, column)
        if piece != 0 and piece.colour == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        return False

    def _move(self, row, column):
        piece = self.board.get_piece(row, column)
        if self.selected and piece == 0 and (row, column) in self.valid_moves:
            self.board.move(self.selected, row, column)
        else:
            return False
        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, column = move
            pygame.draw.circle(self.window, BLUE, (column * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 12)

    def next_turn(self):
        if self.turn == RED:
            self.turn == WHITE
        else:
            self.turn == RED