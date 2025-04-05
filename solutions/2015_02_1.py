import sys

total = 0
for line in sys.stdin:
    l, w, h = map(int, line.strip().split(sep="x"))
    sides = [l * w, w * h, h * l]
    total += 2 * sum(sides) + min(sides)
print(total)
