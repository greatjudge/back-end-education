class CustomList(list):
    def __eq__(self, other):
        return sum(self) == sum(other)

    def __add__(self, other):
        self_size, other_size = len(self), len(other)
        return self.__class__([(self[ind] if ind < self_size else 0) +
                               (other[ind] if ind < other_size else 0) for ind in range(max(self_size,
                                                                                          other_size))])

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        self_size, other_size = len(self), len(other)
        return self.__class__([(self[ind] if ind < self_size else 0) -
                               (other[ind] if ind < other_size else 0) for ind in range(max(self_size,
                                                                                          other_size))])

    def __rsub__(self, other):
        sub = self - other
        return self.__class__([0] * len(sub)) - sub

