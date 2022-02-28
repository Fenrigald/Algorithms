from pympler import asizeof


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self):
        mass = self._length * self._width * 25 * 5 / 1000
        return mass


class Road2:
    __slots__ = ['length', 'width']

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc_mass(self):
        mass = self.length * self.width * 25 * 5 / 1000
        return mass


my_road = Road(20, 5000)
print(asizeof.asizeof(my_road))
my_road = Road2(20, 5000)
print(asizeof.asizeof(my_road))


# Использовал слоты памяти
