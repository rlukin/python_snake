from board import Board


if __name__ == '__main__':
    board = Board(size=30)
    board.set_snake([[x, 3] for x in range(4, 10)] + [[9, y] for y in range(4, 7)])
    board.set_fruits([[0, 1], [7, 5], [10, 23]])
    board.print()
