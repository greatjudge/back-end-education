from itertools import cycle


class User:
    def __init__(self, name: str):
        self.name = name


class TttUser(User):
    def __init__(self, name, mark):
        super().__init__(name)
        self._mark = mark

    @property
    def mark(self):
        return self._mark


class TttField:
    def __init__(self, size: int = 3):
        self.size = size
        self._map = [['_'] * size for _ in range(size)]

    def set_mark(self, row_number: int,
                 column_number: int, mark):
        if self._map[row_number][column_number] == '_':
            self._map[row_number][column_number] = mark
            return True
        else:
            return False
            # raise ValueError(f'map[{row_number}][{column_number}] must be free, '
            #                  f'not {self._map[row_number][column_number]}')

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

    def __str__(self):
        string = ''
        for row in self._map:
            string += ' '.join(row) + '\n'
        return string.rstrip('\n')


class TttGame:
    def __init__(self, size: int, user1: TttUser, user2: TttUser):
        self._gamefield = TttField(size)
        self.user1 = user1
        self.user2 = user2
        self.numbers = self._get_numbers()

    def game(self):
        win_flag = False
        print(self.numbers)
        users = cycle((self.user1, self.user2))
        for i in range(self._gamefield.size ** 2):
            user = next(users)
            print(str(self._gamefield))
            while True:
                number = input(f'{user.name}`s move: ')
                if any((not number.isdigit(),
                       not 0 <= int(number) < self._gamefield.size ** 2)):
                    print(f'{number} is not valid. Put digit, which is less {self._gamefield.size ** 2}')
                    continue
                number = int(number)
                if self._gamefield.set_mark(number // self._gamefield.size,
                                            number % self._gamefield.size,
                                            user.mark):
                    break
                else:
                    print('Field[number] must be free')
                    continue

            if self._gamefield.check_win(number // self._gamefield.size,
                                         number % self._gamefield.size,
                                         user.mark):
                win_flag = True
                print(f'Player {user.name} has won!')
                break
        if not win_flag:
            print('Draw')

    def _get_numbers(self) -> str:
        numbers = ''
        for i in range(self._gamefield.size):
            ' '.join([str(i*self._gamefield.size+j) for j in range(self._gamefield.size)]) + '\n'
        return numbers.rstrip('\n')


if __name__ == '__main__':
    name, mark = input('Write first user`s name and mark: name mark (x or o)').split()
    user1 = TttUser(name, mark)
    name, mark = input('Write first user`s name and mark: name mark (x or o)').split()
    user2 = TttUser(name, mark)
    game = TttGame(3, user1, user2)
    game.game()
