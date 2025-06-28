from functools import partial
from hashlib import md5
from itertools import count


def solve(secret_key: str, n: int) -> int:
    for i in count(1):
        if md5(f"{secret_key}{i}".encode()).hexdigest().startswith(n * "0"):
            return i
    raise Exception("unreachable")


part1 = partial(solve, n=5)
part2 = partial(solve, n=6)


if __name__ == "__main__":
    import aoc

    aoc.main(part1, part2)
