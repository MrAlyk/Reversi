from unittest import TestCase

from .piece import Piece


class TestPiece(TestCase):
    def setUp(self):
        self.piece = Piece('white', 4, 4)

    def test_get_colour(self):
        result = True if self.piece.get_colour() == 'white' else False

        self.assertTrue(result)

    def test_calc_pos(self):
        self.piece.calc_pos()

        self.assertEqual((self.piece.y_pos, self.piece.x_pos),
                         (self.piece.row * (500//8), self.piece.col * (500//8)))

    def test_change_colour_to_black(self):
        self.piece.change_colour('black')

        self.assertEqual(self.piece.get_colour(), 'black')

    def test_change_colour_to_white(self):
        self.piece.change_colour('white')

        self.assertEqual(self.piece.get_colour(), 'white')
