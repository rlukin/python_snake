from board import Board
from curses import wrapper
from time import sleep


def game(stdscr):
    snake = [[4, 3], [4, 4], [4, 5]]
    fruits = [[0, 1], [7, 5], [10, 23]]
    mapping = {258: 'UP',
               259: 'DOWN',
               260: 'LEFT',
               261: 'RIGHT'}
    board = Board(size=30, snake=snake, fruits=fruits)
    stdscr.nodelay(True)
    key = None
    while key != 27:
        stdscr.clear()
        key = stdscr.getch()
        board.change_snake_direction(mapping.get(key, 0))

        board.move_snake()
        board.print(stdscr)
        stdscr.refresh()
        sleep(.2)


if __name__ == '__main__':
    wrapper(game)
