from itertools import cycle
from exceptions import PlayerInputError, SetMarkError
from users import TicTacPlayer


class TicTacBoard:
    def __init__(self, size: int = 3):
        self.size = size
        self._map = self._make_board()
        self._layout = self._make_layout()

    def __str__(self):
        string = ''
        for row in self._map:
            string += ' '.join(row) + '\n'
        return string.rstrip('\n')

    def _make_board(self):
        return [['_'] * self.size for _ in range(self.size)]

    def _make_layout(self):
        string = ''
        for nrow in range(self.size):
            string += ' '.join([str(nrow * self.size + ncol) for ncol in range(self.size)]) + '\n'
        return string.rstrip('\n')

    def set_mark(self, row_number: int,
                 column_number: int, mark):
        if self._map[row_number][column_number] == '_':
            self._map[row_number][column_number] = mark
            return True
        else:
            raise SetMarkError(f'map[{row_number}][{column_number}] must be free, '
                               f'not {self._map[row_number][column_number]}')

    def check_win(self, row_number, column_number, mark):
        vertical = all([self._map[i][column_number] == mark for i in range(self.size)])
        horizontal = all([self._map[row_number][j] == mark for j in range(self.size)])
        diagonal = False
        if row_number == column_number:
            diag1 = all([self._map[i][i] == mark for i in range(self.size)])
            diag2 = all([self._map[i][self.size - i - 1] == mark for i in range(self.size)])
            diagonal = any((diag1, diag2))
        return any((vertical,
                    horizontal,
                    diagonal))

    def show_board(self):
        return str(self)

    def show_extended_board(self):
        string = ''
        for nrow, row in enumerate(self._map):
            string += (' '.join(row) + '\t' +
                       ' '.join([str(nrow * self.size + ncol) for ncol in range(self.size)]) + '\n')
        return string.rstrip()

    def update_board(self):
        self._map = self._make_board()

    @property
    def layout(self):
        return self._layout


class TicTacGame:
    def __init__(self, size: int, first_player: TicTacPlayer, second_player: TicTacPlayer):
        self._gamefield = TicTacBoard(size)
        self.player1 = first_player
        self.player2 = second_player

    def start_game(self):
        self._gamefield.update_board()
        players = cycle((self.player1, self.player2))

        for i in range(self._gamefield.size ** 2):
            player = next(players)
            self._show_extended_board()
            row, column = self._make_move(player)
            if self._gamefield.check_win(row, column, player.mark):
                self._show_greeting(player)
                break
        else:
            self._show_draw()
        self._show_board()

    def _make_move(self, player) -> (int, int):
        while True:
            try:
                number = self._parse_input(input(f'{player.name}`s ({player.mark}) move: '))
                row = number // self._gamefield.size
                column = number % self._gamefield.size # т.к. number = row * size + column
                self._gamefield.set_mark(row, column, player.mark)
            except PlayerInputError as e:
                print(f'Put digit, which is less {self._gamefield.size ** 2}')
            except SetMarkError as e:
                print('Board[number] must be free')
            else:
                break
        return row, column

    def _parse_input(self, player_input: str) -> int:
        if self._validate_input(player_input):
            return int(player_input)

    def _validate_input(self, player_input) -> bool:
        if (not player_input.isdigit() or
                not (0 <= int(player_input) < self._gamefield.size ** 2)):
            raise PlayerInputError(f'{player_input} is not valid. Put digit, which is less {self._gamefield.size ** 2}')
        else:
            return True

    def _show_board(self):
        print(self._gamefield.show_board())

    def _show_extended_board(self):
        print(self._gamefield.show_extended_board())

    def _show_greeting(self, winner: TicTacPlayer):
        print(f'Player {winner.name} has won!')

    def _show_draw(self):
        print('Draw')


if __name__ == '__main__':
    name, mark = input('Write first user`s name and mark: name mark (x or o) ').split()
    user1 = TicTacPlayer(name, mark)
    name, mark = input('Write first user`s name and mark: name mark (x or o) ').split()
    user2 = TicTacPlayer(name, mark)
    game = TicTacGame(3, user1, user2)
    game.start_game()
