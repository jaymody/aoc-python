import sys


def num_vowels(s):
    return sum(c in "aeiou" for c in s)


def contains_consecutive_char(s):
    return any(s[i] == s[i + 1] for i in range(len(s) - 1))


def contains_bad_string(s):
    return any(s[i : i + 2] in {"ab", "cd", "pq", "xy"} for i in range(len(s)))


def is_nice_string(s):
    return (
        num_vowels(s) >= 3
        and contains_consecutive_char(s)
        and not (contains_bad_string(s))
    )


print(sum(is_nice_string(line.strip()) for line in sys.stdin))
