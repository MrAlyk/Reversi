from .const import TILE_IMG, COL_BLACK, ROWS, COLS, TILE_SIZE, font, COL_WHITE
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

    @staticmethod
    def __draw_tiles(win):
        win.fill(COL_BLACK)
        x, y = 0, 0
        for row in range(ROWS):
            x = 0
            for col in range(COLS):
                win.blit(TILE_IMG, (x, y))
                x = x + TILE_SIZE
            y = y + TILE_SIZE

    def __draw_starting_board(self, win):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(None)
                if row == 3 and col == 3:
                    self.board[row][col] = (Piece('white', col, row, win))
                    self.pieces -= 1
                if row == 3 and col == 4:
                    self.board[row][col] = (Piece('black', col, row, win))
                    self.pieces -= 1
                if row == 4 and col == 3:
                    self.board[row][col] = (Piece('black', col, row, win))
                    self.pieces -= 1
                if row == 4 and col == 4:
                    self.board[row][col] = (Piece('white', col, row, win))
                    self.pieces -= 1
        self.draw_info('black')

    def draw(self, win):
        self.__draw_tiles(win)
        self.__draw_starting_board(win)

    def draw_info(self, turn):
        text = font.render(f'Turn: {turn.upper()}', True, COL_WHITE, COL_BLACK)
        self.win.blit(text, (10, 510))

    def draw_winner(self, winner):
        if winner == 'black' or winner == 'white':
            text = font.render(f' {winner.upper()} WON THE GAME !!!', True, COL_WHITE, COL_BLACK)
            self.win.blit(text, (10, 510))
        else:
            text = font.render(f'ITS  A  {winner.upper()} !!!', True, COL_WHITE, COL_BLACK)
            self.win.blit(text, (10, 510))

    def is_on_board(self, col, row):
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
