def part1(text: str) -> int:
    return sum(1 if c == "(" else -1 for c in text)


def part2(text: str) -> int:
    floor = 0
    for i, c in enumerate(text):
        floor += 1 if c == "(" else -1
        if floor < 0:
            return i + 1
    raise Exception("unreachable")


if __name__ == "__main__":
    import aoc

    aoc.main(part1, part2)
