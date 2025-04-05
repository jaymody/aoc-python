x, y, visited = [0, 0], [0, 0], {(0, 0)}
for i, c in enumerate(input().strip()):
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
print(len(visited))
