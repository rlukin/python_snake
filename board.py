from os import system, name
from random import randint

movement = {'UP':    [1, 0],
            'DOWN':  [-1, 0],
            'LEFT':  [0, -1],
            'RIGHT': [0, 1]}


class Board:
    def __init__(self, size=15, snake=[], fruits=[]):
        self._size = size
        self._field = self.get_field(self._size)
        self._snake = snake
        self._fruits = fruits
        self._direction = 'UP'
        self._score = 0

    def set_snake(self, snake):
        self._snake = [[x % self._size, y % self._size] for x, y in snake]

    def set_fruits(self, fruits):
        self._fruits = fruits

    def _eat_fruit(self, fruit_position):
        self._fruits.remove(fruit_position)
        #TODO: refactor
        self._fruits.append([randint(0, self._size-1), randint(0, self._size-1)])
        self._score += 1

    def change_snake_direction(self, direction):
        if direction in movement:
            self._direction = direction

    def move_snake(self):
        head = [sum(x) for x in zip(movement[self._direction], self._snake[0])]
        if head in self._fruits:
            self._eat_fruit(head)
            #TODO: refactor
            self.set_snake([head] + self._snake)
        else:
            self.set_snake([head] + self._snake[:-1])

    @staticmethod
    def get_field(size):
        return ['.' * size] * size

    @staticmethod
    def clear():
        #TODO: remove
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    def print(self, stdscr):
        self.render()
        for index, row in enumerate(self._field):
            stdscr.addstr(index, 0, ' '.join(row))
        stdscr.addstr(self._size, 0, 'Score - {}'.format(self._score))

    def render(self):
        self._field = self.get_field(self._size)
        self.add_objects(self._field, self._fruits, '@')
        self.add_objects(self._field, self._snake, 'O')

    @staticmethod
    def add_objects(field, objects, symbol):
        for x, y in objects:
            field[x] = field[x][:y] + symbol + field[x][y + 1:]
