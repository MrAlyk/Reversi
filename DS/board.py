from .const import ROWS, COLS
from .draw import Draw
from .piece import Piece


class Board:
    def __init__(self, win):
        self.board = []
        self.win = win
        self.pieces = 64
        self.draw(win)

    def update_board(self, col, row, colour, lst):
        self.board[row][col] = Piece(colour, col, row, self.win)
        self.pieces -= 1
        for i in range(len(lst)):
            self.board[lst[i][0]][lst[i][1]].change_colour(colour)

    def create_board(self, win):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(None)
                if row == ROWS / 2 - 1 and col == COLS / 2 - 1:
                    self.board[row][col] = (Piece('white', col, row, win))
                    self.pieces -= 1
                if row == ROWS / 2 - 1 and col == COLS / 2:
                    self.board[row][col] = (Piece('black', col, row, win))
                    self.pieces -= 1
                if row == ROWS / 2 and col == COLS / 2 - 1:
                    self.board[row][col] = (Piece('black', col, row, win))
                    self.pieces -= 1
                if row == ROWS / 2 and col == COLS / 2:
                    self.board[row][col] = (Piece('white', col, row, win))
                    self.pieces -= 1

        Draw.draw_info(win, 'black')

    def draw(self, win):
        Draw.draw_tiles(win)
        self.create_board(win)

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
