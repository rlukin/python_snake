class Board:
    def __init__(self, size=15):
        self._field = ['.' * size] * size

    def print(self):
        for row in self._field:
            print(' '.join(row))
