import math
import sys

total = 0
for line in sys.stdin:
    dims = sorted(map(int, line.strip().split(sep="x")))
    total += 2 * sum(dims[:2]) + math.prod(dims)
print(total)
