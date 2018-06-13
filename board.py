from os import system, name


class Board:
    def __init__(self, size=15):
        self._size = size
        self._field = self.get_field(self._size)
        self._snake = [[x, 3] for x in range(4, 10)] + [[9, y] for y in range(4, 7)]
        self._fruits = [[0, 1], [7, 5], [10, 23]]

    @staticmethod
    def get_field(size):
        return ['.' * size] * size

    @staticmethod
    def clear():
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    def print(self):
        self.clear()
        self.render()
        for row in self._field:
            print(' '.join(row))

    def render(self):
        self._field = self.get_field(self._size)
        self.add_objects(self._field, self._fruits, '@')
        self.add_objects(self._field, self._snake, 'O')

    @staticmethod
    def add_objects(field, objects, symbol):
        for x, y in objects:
            field[x] = field[x][:y] + symbol + field[x][y+1:]
