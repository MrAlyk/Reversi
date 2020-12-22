from .draw import Draw
from .const import TILE_SIZE


class Piece:
    def __init__(self, colour, col, row):
        self.x_pos = 0
        self.y_pos = 0
        self.colour = colour
        self.col = col
        self.row = row
        self.draw()

    def get_colour(self):
        return self.colour

    def calc_pos(self):
        self.x_pos = self.col * TILE_SIZE
        self.y_pos = self.row * TILE_SIZE

    def change_colour(self, colour):
        self.colour = colour
        self.draw()

    def draw(self):
        self.calc_pos()
        Draw.draw_piece(self.colour, self.x_pos, self.y_pos)

    def __repr__(self):
        return f'PIECE OBJ :row.{self.row};col.{self.col} ' + self.colour
