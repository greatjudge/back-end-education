import unittest
from custom_meta import CustomMeta

class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __add__(self, other):
        return self.custom_val + other.custom_val


class TestMeta(unittest.TestCase):
    def test_meta_exists(self):
        inst = CustomClass()
        inst.custom_x
        inst.custom_val
        inst.custom_line()

    def test_meta_error(self):
        inst = CustomClass()
        with self.subTest():
            with self.assertRaises(AttributeError):
                a = inst.x  # ошибка
                a = inst.val  # ошибка
                a = inst.line()  # ошибка

    def test_not_change_magic(self):
        inst = CustomClass(100)
        other = CustomClass(110)
        self.assertEqual(inst.__add__(other), 210)



if __name__ == '__main__':
    unittest.main()