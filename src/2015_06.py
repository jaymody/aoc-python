from typing import NamedTuple, Callable, Generator
from functools import partial


class Coord(NamedTuple):
    row: int
    col: int

    @classmethod
    def of_string(cls, s: str):
        return cls(*map(int, s.split(",")))


class Rect(NamedTuple):
    topleft: Coord
    botright: Coord

    @classmethod
    def of_strings(cls, topleft: str, botright: str):
        return cls(*map(Coord.of_string, (topleft, botright)))

    def __iter__(self) -> Generator[tuple[int, int], None, None]:
        for row in range(self.topleft.row, self.botright.row + 1):
            for col in range(self.topleft.col, self.botright.col + 1):
                yield row, col


def solve(
    text: str,
    on_fn: Callable[[int], int],
    off_fn: Callable[[int], int],
    toggle_fn: Callable[[int], int],
    nrows: int = 1000,
    ncols: int = 1000,
):
    grid = [[0] * ncols for _ in range(nrows)]

    def apply(rect: Rect, fn: Callable[[int], int]):
        for row, col in rect:
            grid[row][col] = fn(grid[row][col])

    for line in text.splitlines():
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


part1 = partial(
    solve,
    on_fn=lambda _: 1,
    off_fn=lambda _: 0,
    toggle_fn=lambda x: 0 if x == 1 else 1,
)

part2 = partial(
    solve,
    on_fn=lambda x: x + 1,
    off_fn=lambda x: max(0, x - 1),
    toggle_fn=lambda x: x + 2,
)

if __name__ == "__main__":
    import aoc

    aoc.main(part1, part2)
