import pygame
from pygame import image

pygame.font.init()

WIDTH, HEIGHT = 500, 500
INFO_HEIGHT = 50
ROWS, COLS = 8, 8
TILE_SIZE = WIDTH // COLS

COL_BLACK = (0, 0, 0)

WHITE_IMG = pygame.transform.scale(image.load('png/White.png'), (TILE_SIZE, TILE_SIZE))

BLACK_IMG = pygame.transform.scale(image.load('png/Black.png'), (TILE_SIZE, TILE_SIZE))

TILE_IMG = pygame.transform.scale(image.load('png/Tile.png'), (TILE_SIZE, TILE_SIZE))

WIN = pygame.display.set_mode((WIDTH, HEIGHT + INFO_HEIGHT))
pygame.display.set_caption('Reversi')
FPS = 60

font = pygame.font.Font('freesansbold.ttf', 32)
COL_WHITE = (255, 255, 255)
