import pygame
from .constants import BLACK, RED, WHITE, ROWS, COLUMNS, SQUARE_SIZE
from .piece import Piece


class Board:
    def __init__(self):
        self.board = []
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

    def move(self, piece, row, column):
        # swap positions
        self.board[piece.row][piece.column], self.board[row][column] = self.board[row][column], \
                                                                       self.board[piece.row][piece.column]
        piece.move(row, column)

        if row == ROWS or row == 0:
            piece.make_king()
            if piece.colour == WHITE:
                self.white_kings += 1
            else:
                self.red_kings += 1

    def get_piece(self, row, column):
        return self.board[row][column]

    def _traverse_left(self, start, stop, step, colour, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            current = self.board.[r][left](r, left)
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

    def _traverse_right(self, start, stop, step, colour, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLUMNS:
                break
            current = self.board.[r][right](r, right)
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
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.colour == RED or piece.king:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.colour, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.colour, right))

        if piece.colour == WHITE or piece.king:
            moves.update(self._traverse_left(row + 1, max(row + 3, 1), 1, piece.colour, left))
            moves.update(self._traverse_right(row + 1, max(row + 3, 1), 1, piece.colour, right))

