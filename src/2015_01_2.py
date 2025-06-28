floor = 0
for i, c in enumerate(input().strip()):
    floor += 1 if c == "(" else -1
    if floor < 0:
        print(i + 1)
        break
