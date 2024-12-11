

def calculate_distinct_positions(grid: list) -> int:
    distinct_positions = set()
    rows = len(grid)
    cols = len(grid[0])

    # Get initial starting position of guard
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "^":
                break
        else:
            continue
        break

    # Guard moving position 
    dr = -1
    dc = 0

    # Loop positions
    while True:
        distinct_positions.add((i, j))
        if i + dr < 0 or i + dr >= rows or j + dc < 0 or j + dc < 0 or j + dc >= cols: 
            break
        if grid[i + dr][j + dc] == "#":
            dc, dr = -dr, dc
        else: # Rotate
            i += dr
            j += dc 

    return len(distinct_positions)


if __name__ == "__main__":
    with open('input.txt', 'r') as guard_map:
        guard_map = guard_map.read().strip().split("\n")
        print(calculate_distinct_positions(guard_map))
        