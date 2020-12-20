from DS import WIN, FPS, TILE_SIZE
import pygame
from DS.game import Game


def get_click_position(pos):
    x, y = pos
    col = x // TILE_SIZE
    row = y // TILE_SIZE

    return col, row


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                col, row = get_click_position(pos)
                game.make_move(col, row)

        pygame.display.update()


main()
