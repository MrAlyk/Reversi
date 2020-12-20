from DS.const import *


class Draw:

    @staticmethod
    def draw_tiles():
        WIN.fill(COL_BLACK)
        x, y = 0, 0
        for row in range(ROWS):
            x = 0
            for col in range(COLS):
                WIN.blit(TILE_IMG, (x, y))
                x = x + TILE_SIZE
            y = y + TILE_SIZE

    @staticmethod
    def draw_piece(colour, x_pos, y_pos):
        if colour == "white":
            WIN.blit(WHITE_IMG, (x_pos, y_pos))
        else:
            WIN.blit(BLACK_IMG, (x_pos, y_pos))

    @staticmethod
    def draw_info(turn):
        text = font.render(f'Turn: {turn.upper()}', True, COL_WHITE, COL_BLACK)
        WIN.blit(text, (10, 510))

    @staticmethod
    def draw_winner(winner):
        if winner == 'black' or winner == 'white':
            text = font.render(f' {winner.upper()} WON THE GAME !!!', True, COL_WHITE, COL_BLACK)
            WIN.blit(text, (10, 510))
        else:
            text = font.render(f'ITS  A  {winner.upper()} !!!', True, COL_WHITE, COL_BLACK)
            WIN.blit(text, (10, 510))
