class Player:
    def __init__(self, name: str):
        self.name = name


class TicTacPlayer(Player):
    def __init__(self, name, mark):
        super().__init__(name)
        self._mark = mark

    @property
    def mark(self):
        return self._mark
