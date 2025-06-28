import sys
from typing import Callable


def main(part1: Callable[[str], str | int], part2: Callable[[str], str | int]):
    match sys.argv:
        case [_, "part1"]:
            print(part1(sys.stdin.read().strip()))
        case [_, "part2"]:
            print(part2(sys.stdin.read().strip()))
        case _:
            raise Exception("must pass in exactly one argument: 'part1' or 'part2'")
