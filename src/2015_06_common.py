import sys
from typing import NamedTuple


class Coord(NamedTuple):
    row: int
    col: int

    def of_string(s):
        return Coord(*map(int, s.split(",")))


class Rect(NamedTuple):
    topleft: Coord
    botright: Coord

    def of_strings(topleft, botright):
        return Rect(*map(Coord.of_string, (topleft, botright)))

    def __iter__(self):
        for row in range(self.topleft.row, self.botright.row + 1):
            for col in range(self.topleft.col, self.botright.col + 1):
                yield row, col


def solve(on_fn, off_fn, toggle_fn, nrows=1000, ncols=1000):
    grid = [[0] * ncols for _ in range(nrows)]

    def apply(rect, fn):
        for row, col in rect:
            grid[row][col] = fn(grid[row][col])

    for line in sys.stdin:
        match line.strip().split():
            case ["turn", "on", topleft, "through", botright]:
                fn = on_fn
            case ["turn", "off", topleft, "through", botright]:
                fn = off_fn
            case ["toggle", topleft, "through", botright]:
                fn = toggle_fn
            case _:
                raise Exception(f"could not parse line: {line}")
        rect = Rect.of_strings(topleft, botright)
        apply(rect, fn)

    return sum(x for row in grid for x in row)
