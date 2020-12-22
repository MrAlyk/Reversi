from .const import ROWS, COLS
from .draw import Draw
from .piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.emptyTiles = 64
        self.draw()

    def update_board(self, col, row, colour, lst):
        self.board[row][col] = Piece(colour, col, row)
        self.deduct_tile()
        for i in range(len(lst)):
            self.board[lst[i][0]][lst[i][1]].change_colour(colour)

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(None)
        self.put_starting_pieces()
        Draw.draw_info('black')

    def put_starting_pieces(self):
        self.put_piece(COLS // 2 - 1, ROWS // 2 - 1, 'white')
        self.put_piece(COLS // 2, ROWS // 2 - 1, 'black')
        self.put_piece(COLS // 2 - 1, ROWS // 2, 'black')
        self.put_piece(COLS // 2, ROWS // 2, 'white')

    def put_piece(self, col, row, colour):
        self.board[row][col] = (Piece(colour, col, row))
        self.deduct_tile()

    def draw(self):
        Draw.draw_tiles()
        self.create_board()

    @staticmethod
    def is_on_board(col, row):
        if COLS > col > -1 and ROWS > row > -1:
            return True
        else:
            return False

    def tile_not_empty(self, col, row):
        if self.board[row][col] is not None:
            return True
        else:
            return False

    def is_not_valid_tile(self, col, row):
        if not self.is_on_board(col, row) or not self.tile_not_empty(col, row):
            return True
        else:
            return False

    def deduct_tile(self):
        self.emptyTiles -= 1
