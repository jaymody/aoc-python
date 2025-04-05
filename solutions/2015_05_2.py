import sys


def contains_non_consecutive_pairs(s):
    return any(
        s[i : i + 2] == s[j : j + 2]
        for i in range(len(s))
        for j in range(i + 2, len(s))
    )


def contains_sandwich(s):
    return any(s[i] == s[i + 2] for i in range(len(s) - 2))


def is_nice_string(s):
    return contains_non_consecutive_pairs(s) and contains_sandwich(s)


print(sum(is_nice_string(line.strip()) for line in sys.stdin))
