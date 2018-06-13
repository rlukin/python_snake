from os import system, name


class Board:
    def __init__(self, size=15, snake=[], fruits=[]):
        self._size = size
        self._field = self.get_field(self._size)
        self._snake = snake
        self._fruits = fruits

    def set_snake(self, snake):
        self._snake = snake

    def set_fruits(self, fruits):
        self._fruits = fruits

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
