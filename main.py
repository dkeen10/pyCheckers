import pygame
from checkers.constants import WIDTH, HEIGHT
from checkers.board import Board


FPS = 60

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")


def main():
    run = True
    board = Board()

    # setting framerat:
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)

        # checking events types:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        # board.draw_squares(WINDOW)
        board.draw(WINDOW)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
