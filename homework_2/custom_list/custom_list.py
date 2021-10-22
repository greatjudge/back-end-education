class CustomList(list):
    def __eq__(self, other):
        return sum(self) == sum(other)

    def __add__(self, other):
        self_size, other_size = len(self), len(other)
        if self_size > other_size:
            right = list(other) + [0] * (self_size - other_size)
            return self.__class__([val + right[ind] for ind, val in enumerate(self)])
        elif self_size < other_size:
            left = list(self) + [0] * (other_size - self_size)
            return self.__class__([val + other[ind] for ind, val in enumerate(left)])
        return self.__class__([val + other[ind] for ind, val in enumerate(self)])

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        self_size, other_size = len(self), len(other)
        if self_size > other_size:
            right = list(other) + [0] * (self_size - other_size)
            return self.__class__([val - right[ind] for ind, val in enumerate(self)])
        elif self_size < other_size:
            left = list(self) + [0] * (other_size - self_size)
            return self.__class__([val - other[ind] for ind, val in enumerate(left)])
        return self.__class__([val - other[ind] for ind, val in enumerate(self)])

    def __rsub__(self, other):
        sub = self - other
        return self.__class__([0] * len(sub)) - sub

