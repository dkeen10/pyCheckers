import pygame
from .constants import BLACK, RED, WHITE, ROWS, COLUMNS, SQUARE_SIZE
from .piece import Piece


class Board:
    """
    Represents a Checkers Board.
    """

    def __init__(self):
        """
        Initialize a new Board.
        """
        self.board = []
        self.red_remaining = 12
        self.white_remaining = 12
        self.red_kings = 0
        self.white_kings = 0
        self.create_board()

    def draw_squares(self, window):
        """
        Draw board squares.

        :param window: the pygame window
        """
        window.fill(BLACK)
        for row in range(ROWS):
            for column in range(row % 2, COLUMNS, 2):
                pygame.draw.rect(window, RED, (row * SQUARE_SIZE, column * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        """
        Create a Checkers Board.
        """
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
        """
        Draw the current Board state.

        :param window: the pygame window
        """
        self.draw_squares(window)
        for row in range(ROWS):
            for column in range(COLUMNS):
                piece = self.board[row][column]
                if piece != 0:
                    piece.draw(window)

    def move(self, piece, row, column):
        """
        Move a Checkers piece.

        :param piece: a piece object
        :param row: an int
        :param column: an int
        :return: the new position of the checkers piece as an object
        """
        # swap positions
        self.board[piece.row][piece.column], self.board[row][column] = self.board[row][column], \
                                                                       self.board[piece.row][piece.column]
        piece.move(row, column)

        if (row == ROWS - 1 or row == 0) and not piece.king():
            piece.make_king()
            if piece.colour == WHITE:
                self.white_kings += 1
            elif piece.colour == RED:
                self.red_kings += 1

    def get_piece(self, row, column):
        """
        Get the specified Checkers piece.

        :param row: an int
        :param column: an int
        :return: the specified Checkers piece as an int
        """

        return self.board[row][column]

    def remove(self, pieces):
        """
        Remove the specified piece from the game.

        :param pieces: an array of piece objects
        """
        for piece in pieces:
            self.board[piece.row][piece.column] = 0
            if piece != 0:
                if piece.colour == RED:
                    self.red_remaining -= 1
                else:
                    self.white_remaining -= 1

    def check_winner(self):
        """
        Check if there is a winner.

        :return: WHITE if RED has no pieces remaining, RED if WHITE hsa no pieces remaining, else None
        """
        if self.red_remaining <= 0:
            return WHITE
        elif self.white_remaining <= 0:
            return RED
        return None

    def _traverse_left(self, start, stop, step, colour, left, skipped=None):
        """
        Check if there valid moves to the left of the specified piece.

        :param start: an int representing the row at the start of the move
        :param stop: and int representing the row at the end of the move
        :param step: an int representing how many rows to move per action
        :param colour: an rgb colour
        :param left: the direction to move
        :param skipped: an array of coordinates representing the pieces that can be captured
        :return: the potential moves as coordinate arrays
        """
        if skipped is None:
            skipped = []
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            current = self.board[r][left]
            if current == 0:  # if traversing to empty square
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._traverse_left(r + step, row, step, colour, left - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, colour, left + 1, skipped=last))
                break
            elif current.colour == colour:  # if traversing square has a same colour piece, return
                break
            else:  # if traversing square has a different colour piece, recursively call current
                last = [current]
            left -= 1
        return moves

    def _traverse_right(self, start, stop, step, colour, right, skipped=None):
        """
        Check if there valid moves to the right of the specified piece.

        :param start: an int representing the row at the start of the move
        :param stop: and int representing the row at the end of the move
        :param step: an int representing how many rows to move per action
        :param colour: an rgb colour
        :param right: the direction to move
        :param skipped: an array of coordinates representing the pieces that can be captured
        :return: the potential moves as coordinate arrays
        """
        if skipped is None:
            skipped = []
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLUMNS:
                break
            current = self.board[r][right]
            if current == 0:  # if traversing to empty square
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._traverse_left(r + step, row, step, colour, right - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, colour, right + 1, skipped=last))
                break
            elif current.colour == colour:  # if traversing square has a same colour piece, return
                break
            else:  # if traversing square has a different colour piece, recursively call current
                last = [current]
            right += 1
        return moves

    def get_valid_moves(self, piece):
        """
        Get the valid moves for the specified piece.

        :param piece: a Piece object
        :return: the valid moves as coordinate arrays.
        """
        moves = {}
        left = piece.column - 1
        right = piece.column + 1
        row = piece.row

        if piece.colour == RED or piece.king:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.colour, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.colour, right))

        if piece.colour == WHITE or piece.king:
            moves.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, piece.colour, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, piece.colour, right))

        return moves
