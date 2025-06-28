def part1(text: str) -> int:
    x, y, visited = 0, 0, {(0, 0)}
    for c in text:
        match c:
            case "^":
                y += 1
            case "v":
                y -= 1
            case ">":
                x += 1
            case "<":
                x -= 1
            case _:
                raise Exception(f"invalid char {c}")
        visited.add((x, y))
    return len(visited)


def part2(text: str) -> int:
    x, y, visited = [0, 0], [0, 0], {(0, 0)}
    for i, c in enumerate(text):
        i = i % 2
        match c:
            case "^":
                y[i] += 1
            case "v":
                y[i] -= 1
            case ">":
                x[i] += 1
            case "<":
                x[i] -= 1
            case _:
                raise Exception(f"invalid char {c}")
        visited.add((x[i], y[i]))
    return len(visited)


if __name__ == "__main__":
    import aoc

    aoc.main(part1, part2)
