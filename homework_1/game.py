from itertools import cycle
from typing import List

from exceptions import PlayerInputError, SetMarkError, InterruptedGameError
from users import TicTacPlayer


Board = List[List[str]]


class TicTacBoard:
    def __init__(self, size: int = 3):
        self.size = size
        self._map = self._make_board(self.size)
        self._layout = self._make_layout()

    def __str__(self):
        string = ''
        for row in self._map:
            string += ' '.join(row) + '\n'
        return string.rstrip('\n')

    @staticmethod
    def _make_board(size: int) -> Board:
        return [['_'] * size for _ in range(size)]

    def _make_layout(self):
        string = ''
        for nrow in range(self.size):
            string += ' '.join([str(nrow * self.size + ncol)
                                for ncol in range(self.size)]) + '\n'
        return string.rstrip('\n')

    def _validate_indexes(self, row_number, column_number):
        if not 0 <= int(row_number) < self.size:
            raise IndexError(f'row_number must be less {self.size} and larger 0')
        if not 0 <= int(column_number) < self.size:
            raise IndexError(f'column_number must be less {self.size} and larger 0')

    def set_mark(self, row_number: int,
                 column_number: int, mark: str):
        self._validate_indexes(row_number, column_number)
        if not isinstance(mark, str):
            raise SetMarkError
        if self._map[row_number][column_number] == '_':
            self._map[row_number][column_number] = mark
        else:
            raise SetMarkError

    def check_win(self, row_number, column_number, mark):
        self._validate_indexes(row_number, column_number)
        vertical = all((self._map[i][column_number] == mark for i in range(self.size)))
        horizontal = all((self._map[row_number][j] == mark for j in range(self.size)))
        diagonal = False
        if any((row_number == column_number, # If diagonal
               row_number == self.size - 1 - column_number,
               column_number == self.size - 1 - row_number)) :
            diag1 = all((self._map[i][i] == mark for i in range(self.size)))
            diag2 = all((self._map[i][self.size - i - 1] == mark for i in range(self.size)))
            diagonal = any((diag1, diag2))
        return any((vertical,
                    horizontal,
                    diagonal))

    def board(self):
        return str(self)

    def extended_board(self):
        string = ''
        for nrow, row in enumerate(self._map):
            string += (' '.join([str(nrow * self.size + ncol)
                                for ncol in range(self.size)])
                       + '\t' + ' '.join(row) + '\n')
        return string.rstrip()

    @property
    def layout(self):
        return self._layout

    def update_board(self):
        self._map = self._make_board(self.size)


class TicTacGame:
    quit_code = 'q'

    def __init__(self, size: int = 3):
        self._size = size
        self._gamefield = TicTacBoard(self._size)

    def show_instructions(self):
        instructions = 'TicTak Game.\n First player: x, ' \
                       'Second player: o. Enter the number to put the symbol\n'
        quit_instructions = f' Type \'{self.quit_code}\' to quit\n'
        print(instructions + quit_instructions)

    def start_game(self, first_name: str, second_name: str):
        self._gamefield.update_board()
        self.show_instructions()
        self._game(TicTacPlayer(first_name, 'x'),
                   TicTacPlayer(second_name, 'o'))

    def _game(self, player1, player2):
        players = cycle((player1, player2))
        for _ in range(self._gamefield.size ** 2):
            player = next(players)
            self._show_extended_board()

            try:
                row, column = self._make_move(player)
            except InterruptedGameError:
                print('The game is interrupted')
                break

            if self._gamefield.check_win(row, column, player.mark):
                self._show_board()
                self._show_greeting(player)
                break
        else:
            self._show_board()
            self._show_draw()

    def _make_move(self, player):
        while True:
            try:
                number = self._parse_input(self._player_input(player))
                row = number // self._gamefield.size
                column = number % self._gamefield.size # т.к. number = row * size + column
                self._gamefield.set_mark(row, column, player.mark)
            except PlayerInputError as ex:
                print(ex)
            except SetMarkError:
                print('Board[number] must be free')
            else:
                break
        return row, column

    def _parse_input(self, player_input: str) -> int:
        if player_input == self.quit_code:
            raise InterruptedGameError()
        return int(self._validate_input(player_input))

    def _validate_input(self, player_input) -> str:
        if (not player_input.isdigit() or
                not 0 <= int(player_input) < self._gamefield.size ** 2):
            raise PlayerInputError(f'{player_input} is not valid. '
                                   f'Put digit, which is less {self._gamefield.size ** 2}')
        return player_input

    def _show_board(self):
        print(self._gamefield.board())

    def _show_extended_board(self):
        print(self._gamefield.extended_board())

    @staticmethod
    def _show_greeting(winner: TicTacPlayer):
        print(f'Player {winner.name} has won!')

    @staticmethod
    def _show_draw():
        print('Draw')

    @staticmethod
    def _player_input(player):
        return input(f'{player.name}`s ({player.mark}) move: ').strip()


if __name__ == '__main__':
    name_1 = input('Enter first user`s name: ')
    name_2 = input('Enter second user`s name: ')
    game = TicTacGame()
    game.start_game(name_1, name_2)
