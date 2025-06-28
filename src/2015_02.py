import math


def part1(text: str) -> int:
    total = 0
    for line in text.splitlines():
        l, w, h = map(int, line.strip().split(sep="x"))
        sides = [l * w, w * h, h * l]
        total += 2 * sum(sides) + min(sides)
    return total


def part2(text: str) -> int:
    total = 0
    for line in text.splitlines():
        dims = sorted(map(int, line.strip().split(sep="x")))
        total += 2 * sum(dims[:2]) + math.prod(dims)
    return total


if __name__ == "__main__":
    import aoc

    aoc.main(part1, part2)
