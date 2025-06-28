def part1(text: str) -> int:
    def num_vowels(s: str) -> int:
        return sum(c in "aeiou" for c in s)

    def contains_consecutive_char(s: str) -> bool:
        return any(s[i] == s[i + 1] for i in range(len(s) - 1))

    def contains_bad_string(s: str) -> bool:
        return any(s[i : i + 2] in {"ab", "cd", "pq", "xy"} for i in range(len(s)))

    def is_nice_string(s: str) -> bool:
        return (
            num_vowels(s) >= 3
            and contains_consecutive_char(s)
            and not (contains_bad_string(s))
        )

    return sum(is_nice_string(line.strip()) for line in text.splitlines())


def part2(text: str) -> int:
    def contains_non_consecutive_pairs(s: str) -> bool:
        return any(
            s[i : i + 2] == s[j : j + 2]
            for i in range(len(s))
            for j in range(i + 2, len(s))
        )

    def contains_sandwich(s: str) -> bool:
        return any(s[i] == s[i + 2] for i in range(len(s) - 2))

    def is_nice_string(s: str) -> bool:
        return contains_non_consecutive_pairs(s) and contains_sandwich(s)

    return sum(is_nice_string(line.strip()) for line in text.splitlines())


if __name__ == "__main__":
    import aoc

    aoc.main(part1, part2)
