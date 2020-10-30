import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE
from checkers.game import Game

FPS = 60

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")


def get_row_col_from_mouse(pos):
    """
    Gets the position from the mouse pointer.

    :param pos: an x,y coordinate.

    :return: the row and column on the board as an int that the mouse is pointing to.
    """
    x, y = pos
    row = y // SQUARE_SIZE
    column = x // SQUARE_SIZE
    return row, column


def main():
    """
    Drives the program.
    """
    run = True
    game = Game(WINDOW)

    # setting framerate:
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)

        if game.winner() is not None:
            print(f"{game.winner()} has won!")
            run = False

        # checking events types:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, column = get_row_col_from_mouse(pos)
                game.select(row, column)
        game.update()
    pygame.quit()


if __name__ == "__main__":
    main()
