import unittest

from game import TicTacBoard, TicTacGame
from exceptions import SetMarkError, PlayerInputError, InterruptedGameError


class BoardSetMarkTest(unittest.TestCase):
    def setUp(self):
        self.size = 5
        self.board = TicTacBoard(self.size)

    def test_valid_set(self):
        with self.subTest():
            for number in range(self.board.size ** 2):
                i = number // self.board.size
                j = number % self.board.size
                self.board.set_mark(i, j, str(number))
                self.assertEqual(str(number), self.board._map[i][j])

    def test_invalid_set(self):
        j = self.board.size - 1
        less_number = -10
        larger_number = self.board.size + 10
        not_number_list = ('1', 'kdslk', [1, 2])
        with self.subTest():
            with self.assertRaises(IndexError):
                self.board.set_mark(less_number, j, 'q')
                self.board.set_mark(larger_number, j, 'q')
                self.board.set_mark(j, less_number, 'q')
                self.board.set_mark(j, larger_number, 'q')
            with self.assertRaises(TypeError):
                for obj in not_number_list:
                    self.board.set_mark(0, obj, 'q')
                    self.board.set_mark(obj, 0, 'q')

    def test_not_str_set(self):
        not_str_list = (1, dict(), [1, 2])
        with self.subTest():
            with self.assertRaises(SetMarkError):
                for obj in not_str_list:
                    self.board.set_mark(0, 0, obj)

    def test_not_free_set(self):
        i, j = 0, 0
        self.board.set_mark(i, j, 'no free')
        with self.assertRaises(SetMarkError):
            self.board.set_mark(i, j, 'damn')


class BoardCheckWinTest(unittest.TestCase):
    def setUp(self):
        self.size = 3
        self.board = TicTacBoard(self.size)
        self.win_boards = {
            ((0, 0), (0, 1), (0, 2)): [['x', 'x', 'x'], ['_', '_', '_'], ['_', '_', '_']],
            ((1, 0), (1, 1), (1, 2)): [['_', '_', '_'], ['x', 'x', 'x'], ['_', '_', '_']],
            ((2, 0), (2, 1), (2, 2)): [['_', '_', '_'], ['_', '_', '_'], ['x', 'x', 'x']],
            ((0, 0), (1, 0), (2, 0)): [['x', '_', '_'], ['x', '_', '_'], ['x', '_', '_']],
            ((0, 1), (1, 1), (2, 1)): [['_', 'x', '_'], ['_', 'x', '_'], ['_', 'x', '_']],
            ((0, 2), (1, 2), (2, 2)): [['_', '_', 'x'], ['_', '_', 'x'], ['_', '_', 'x']],
            ((0, 0), (1, 1), (2, 2)): [['x', '_', '_'], ['_', 'x', '_'], ['_', '_', 'x']],
            ((0, 2), (1, 1), (0, 2)): [['_', '_', 'x'], ['_', 'x', '_'], ['x', '_', '_']]
        }
        false_win_boards = []
        draw_boards = []

    def test_true_win(self):
        with self.subTest():
            for indexes, board in self.win_boards.items():
                self.board._map = board
                for row, column in indexes:
                    self.assertTrue(self.board.check_win(row, column, 'x'))

    def test_false_win(self):
        pass

    def test_draw(self):
        pass


class GameParseInputTest(unittest.TestCase):
    def setUp(self):
        self.size = 5
        self.game = TicTacGame(self.size)

    def test_valid_input(self):
        pl_input = '4'
        self.assertEqual(self.game._parse_input(pl_input), 4)

    def test_invalid_input(self):
        pl_input = '5 klop'
        with self.assertRaises(PlayerInputError):
            self.game._parse_input(pl_input)

    def test_interrupt(self):
        pl_input = self.game.quit_code
        with self.assertRaises(InterruptedGameError):
            self.game._parse_input(pl_input)


if __name__ == '__main__':
    unittest.main()