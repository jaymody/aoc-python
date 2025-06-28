x, y, visited = 0, 0, {(0, 0)}
for c in input().strip():
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
print(len(visited))
