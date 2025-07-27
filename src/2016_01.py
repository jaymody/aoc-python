def move(dx: int, dy: int, dir: int, dist: int):
    match dir:
        case 0:
            dy += dist
        case 1:
            dx += dist
        case 2:
            dy -= dist
        case 3:
            dx -= dist
        case _:
            raise Exception("unreachable")
    return dx, dy


def part1(text: str) -> int:
    dx, dy, dir = 0, 0, 0
    for s in text.split(", "):
        rotate, dist = s[0], int(s[1:])
        dir = (dir + 1) % 4 if rotate == "R" else ((dir - 1) % 4)
        dx, dy = move(dx, dy, dir, dist)
    return abs(dy) + abs(dx)


def part2(text: str) -> int:
    dx, dy, dir = 0, 0, 0
    visited = {(dx, dy)}
    for s in text.split(", "):
        rotate, dist = s[0], int(s[1:])
        dir = (dir + 1) % 4 if rotate == "R" else ((dir - 1) % 4)
        for _ in range(0, dist):
            dx, dy = move(dx, dy, dir, 1)
            if (dx, dy) in visited:
                return abs(dx) + abs(dy)
            visited.add((dx, dy))
    raise Exception("no location was visited twice")


if __name__ == "__main__":
    import aoc

    aoc.main(part1, part2)
