import pygame

WIDTH = 600
HEIGHT = 600
ROWS = 8
COLUMNS = 8
SQUARE_SIZE = WIDTH // COLUMNS

# colours:
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

CROWN = pygame.image.load('assests/crown.png')
pygame.transform.scale(CROWN, (43, 23))
