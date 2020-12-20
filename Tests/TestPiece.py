import unittest


from DS import Piece


class TestPiece(unittest.TestCase):
    def setUp(self):
        self.piece = Piece('white', 4, 4)

    def test_accept_changed_color_to_black(self):
        self.piece.change_colour('black')

        result = True if self.piece.get_colour() == 'black' else False

        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
