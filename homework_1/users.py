class TicTacPlayer:
    def __init__(self, name: str, mark: str):
        self.name = name
        self._mark = mark

    @property
    def mark(self) -> str:
        return self._mark
