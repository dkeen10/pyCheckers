import pygame
from .board import Board
from .constants import RED, WHITE, BLUE, SQUARE_SIZE


class Game:
    """
    Represents a Game of Checkers.
    """

    def __init__(self, window):
        """
        Initialize a new game of Checkers.

        :param window: the pygame window
        """
        self._init()
        self.window = window

    def _init(self):
        """
        Initialize certain elements of the Checkers Game.
        """
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    def reset(self):
        """
        Reset the board to the starting state.
        """
        self._init()

    def update(self):
        """
        Update the window to the current board state.
        """
        self.board.draw(self.window)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def select(self, row, column):
        """
        Select the piece that has been clicked on.

        :param row: an int
        :param column: an int
        :return: True if the selected piece is the correct colour for the turn and has valid moves, else False
        """
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
        """
        Move the specified piece.

        :param row: an int
        :param column: an int
        :return: True if the move is successfully made, else False
        """
        piece = self.board.get_piece(row, column)
        if self.selected and piece == 0 and (row, column) in self.valid_moves:
            self.board.move(self.selected, row, column)
            skipped = self.valid_moves[(row, column)]
            if skipped:
                self.board.remove(skipped)
            self.next_turn()
        else:
            return False
        return True

    def draw_valid_moves(self, moves):
        """
        Draw the valid moves for the selected piece.

        :param moves: a coordinate array.
        """
        for move in moves:
            row, column = move
            pygame.draw.circle(self.window, BLUE, (column * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 12)

    def next_turn(self):
        """
        Move to the next player's turn.
        """
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED

    def winner(self):
        """
        Determine the winner of the game.
        :return: WHITE if RED has no pieces remaining, RED if WHITE hsa no pieces remaining, else None
        """
        return self.board.check_winner()
