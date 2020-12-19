from DS.const import *


class Draw:

    @staticmethod
    def draw_tiles(win):
        win.fill(COL_BLACK)
        x, y = 0, 0
        for row in range(ROWS):
            x = 0
            for col in range(COLS):
                win.blit(TILE_IMG, (x, y))
                x = x + TILE_SIZE
            y = y + TILE_SIZE

    @staticmethod
    def draw_piece(colour, win, x_pos, y_pos):
        if colour == "white":
            win.blit(WHITE_IMG, (x_pos, y_pos))
        else:
            win.blit(BLACK_IMG, (x_pos, y_pos))

    @staticmethod
    def draw_info(win, turn):
        text = font.render(f'Turn: {turn.upper()}', True, COL_WHITE, COL_BLACK)
        win.blit(text, (10, 510))

    @staticmethod
    def draw_winner(win, winner):
        if winner == 'black' or winner == 'white':
            text = font.render(f' {winner.upper()} WON THE GAME !!!', True, COL_WHITE, COL_BLACK)
            win.blit(text, (10, 510))
        else:
            text = font.render(f'ITS  A  {winner.upper()} !!!', True, COL_WHITE, COL_BLACK)
            win.blit(text, (10, 510))

