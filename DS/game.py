from DS import Board, ROWS, COLS


class Game(Board):

    def __init__(self, win):
        super().__init__(win)
        self.turn = 'black'
        self.piecesToFlip = []

    def change_turn(self):
        if self.turn == 'black':
            self.turn = 'white'
        else:
            self.turn = 'black'

    def game_over(self):
        if self.pieces < 1:
            return True
        else:
            if self.turn == 'black' and not self.search_for_any_valid_move():
                self.change_turn()
                if not self.search_for_any_valid_move():
                    return True
                else:
                    self.change_turn()
                    return False
            elif self.turn == 'white' and not self.search_for_any_valid_move():
                self.change_turn()
                if not self.search_for_any_valid_move():
                    return True
                else:
                    self.change_turn()
                    return False
            else:
                return False

    def who_won(self):
        blackCount = 0
        whiteCount = 0
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col].get_colour() == 'black':
                    blackCount += 1
                elif self.board[row][col].get_colour() == 'white':
                    whiteCount += 1

        if blackCount > whiteCount:
            return 'black'
        elif whiteCount > blackCount:
            return 'white'
        else:
            return 'tie'

    def is_valid_move(self, col, row):
        self.get_pieces_to_flip(col, row)
        if len(self.piecesToFlip) > 0 and not self.tile_not_empty(col, row):
            return True
        else:
            return False

    def make_move(self, col, row):
        if self.is_valid_move(col, row):
            self.update_board(col, row, self.turn, self.piecesToFlip)
            self.change_turn()
            self.draw_info(self.turn)

    def get_pieces_to_flip(self, col, row):
        self.piecesToFlip = []
        for x, y in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
            rowTemp = row + y
            colTemp = col + x

            if not self.is_on_board(colTemp, rowTemp) or not self.tile_not_empty(colTemp, rowTemp):
                continue

            while self.board[rowTemp][colTemp].get_colour() != self.turn:
                rowTemp += y
                colTemp += x
                if not self.is_on_board(colTemp, rowTemp) or not self.tile_not_empty(colTemp, rowTemp):
                    break
                else:
                    if self.board[rowTemp][colTemp].get_colour() == self.turn:
                        while True:
                            rowTemp -= y
                            colTemp -= x
                            if colTemp == col and rowTemp == row:
                                break
                            self.piecesToFlip.append([rowTemp, colTemp])
                if not self.is_on_board(colTemp, rowTemp) or not self.tile_not_empty(colTemp, rowTemp):
                    break

    def search_for_any_valid_move(self):
        for y in range(8):
            for x in range(8):
                if not self.tile_not_empty(x, y):
                    self.get_pieces_to_flip(x, y)
                else:
                    continue
                if len(self.piecesToFlip) > 0:
                    return True
        return False

    def game_turn(self):
        if not self.search_for_any_valid_move():
            self.change_turn()
