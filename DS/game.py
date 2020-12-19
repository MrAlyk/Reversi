from DS import Board, ROWS, COLS, Draw


class Game:

    def __init__(self, win):
        self.turn = 'black'
        self.win = win
        self.piecesToFlip = []
        self.gameBoard = Board(win)

    def change_turn(self):
        if self.turn == 'black':
            self.turn = 'white'
        else:
            self.turn = 'black'
        Draw.draw_info(self.win, self.turn)

    def game_over(self):
        if self.gameBoard.emptyTiles < 1:
            return True
        else:
            return self.check_turns()

    def check_turns(self):
        if not self.search_for_any_valid_move():
            return self.check_opposite_turn()
        else:
            return False

    def check_opposite_turn(self):
        self.change_turn()
        if not self.search_for_any_valid_move():
            return True
        else:
            self.change_turn()
            return False

    def who_won(self):
        blackCount = 0
        whiteCount = 0
        blackCount, whiteCount = self.count_tiles(blackCount, whiteCount)

        if blackCount > whiteCount:
            return 'black'
        elif whiteCount > blackCount:
            return 'white'
        else:
            return 'tie'

    def count_tiles(self, blackCount, whiteCount):
        for row in range(ROWS):
            for col in range(COLS):
                if self.gameBoard.board[row][col].get_colour() == 'black' \
                        and not self.gameBoard.is_not_valid_tile(col, row):
                    blackCount += 1
                elif self.gameBoard.board[row][col].get_colour() == 'white' \
                        and not self.gameBoard.is_not_valid_tile(col, row):
                    whiteCount += 1
        return blackCount, whiteCount

    def is_valid_move(self, col, row):
        self.get_pieces_to_flip(col, row)
        if len(self.piecesToFlip) > 0 and not self.gameBoard.tile_not_empty(col, row):
            return True
        else:
            return False

    def make_move(self, col, row):
        if self.is_valid_move(col, row):
            self.gameBoard.update_board(col, row, self.turn, self.piecesToFlip)
            self.change_turn()

    def get_pieces_to_flip(self, col, row):
        self.piecesToFlip = []
        for x, y in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
            rowTemp = row + y
            colTemp = col + x

            if self.gameBoard.is_not_valid_tile(colTemp, rowTemp):
                continue
            try:
                self.go_straight(col, colTemp, row, rowTemp, x, y)
            except AttributeError:
                continue

    def go_straight(self, col, colTemp, row, rowTemp, x, y):
        while self.gameBoard.board[rowTemp][colTemp].get_colour() != self.turn:
            rowTemp += y
            colTemp += x
            if self.gameBoard.is_not_valid_tile(colTemp, rowTemp):
                break
            else:
                if self.gameBoard.board[rowTemp][colTemp].get_colour() == self.turn:
                    colTemp, rowTemp = self.backtrack(col, colTemp, row, rowTemp, x, y)

    def backtrack(self, col, colTemp, row, rowTemp, x, y):
        while True:
            rowTemp -= y
            colTemp -= x
            if colTemp == col and rowTemp == row:
                break
            self.piecesToFlip.append([rowTemp, colTemp])
        return colTemp, rowTemp

    def search_for_any_valid_move(self):
        for y in range(ROWS):
            for x in range(COLS):
                if not self.gameBoard.tile_not_empty(x, y):
                    self.get_pieces_to_flip(x, y)
                else:
                    continue
                if len(self.piecesToFlip) > 0:
                    return True
        return False

    def check_turn(self):
        if not self.search_for_any_valid_move():
            self.change_turn()
