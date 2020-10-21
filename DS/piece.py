from .const import TILE_SIZE, WHITE_IMG, BLACK_IMG


class Piece:
    def __init__(self, colour, col, row, win):
        self.x_pos = 0
        self.y_pos = 0
        self.colour = colour
        self.col = col
        self.row = row
        self.win = win
        self.__draw_piece(win)

    def get_colour(self):
        return self.colour

    def calc_pos(self):
        self.x_pos = self.col * TILE_SIZE
        self.y_pos = self.row * TILE_SIZE

    def change_colour(self, colour):
        self.colour = colour
        self.__draw_piece(self.win)

    def __draw_piece(self, win):
        self.calc_pos()
        if self.colour == "white":
            win.blit(WHITE_IMG, (self.x_pos, self.y_pos))
        else:
            win.blit(BLACK_IMG, (self.x_pos, self.y_pos))

    def __repr__(self):
        return f'PIECE OBJ :row.{self.row};col.{self.col} ' + self.colour
