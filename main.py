import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE
from checkers.board import Board
from checkers.game import Game

FPS = 60

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    column = x // SQUARE_SIZE
    return row, column

# def move_with_mouse()


def main():
    run = True
    game = Game(WINDOW)

    # setting framerate:
    clock = pygame.time.Clock()

    # piece = board.get_piece(0, 1)
    # board.move(piece, 4, 3)

    while run:
        clock.tick(FPS)

        # checking events types:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, column = get_row_col_from_mouse(pos)
                # piece = board.get_piece(row, column)
                # board.move(piece, 4, 3)

        game.update()
        # board.draw_squares(WINDOW)
        # board.draw(WINDOW)
        # pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
