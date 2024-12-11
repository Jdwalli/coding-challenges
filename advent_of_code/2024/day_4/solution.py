
def position_grid() -> list:
    return [(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1]]


def count_xmas_appearances(grid: list) -> int:
    count = 0

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == "X":
                for pos_r, pos_c in position_grid():
                    if pos_r == pos_c == 0:
                        continue
                    if not (0 <= x + 3 * pos_r < len(grid) and 0 <= y + 3 * pos_c < len(grid[0])):
                        continue
                    if (grid[x + pos_r][y + pos_c] == "M"
                                and
                                grid[x + 2 * pos_r][y + 2 * pos_c] == "A"
                                and
                                grid[x + 3 * pos_r][y + 3 * pos_c] == "S"
                            ):
                        count += 1
            else:
                continue

    return count


def count_x_mas_appearances(grid: list) -> int:
    count = 0
    for x in range(1, len(grid) - 1):
        for y in range(1, len(grid[0]) - 1):
            if grid[x][y] == "A":
                corners = [grid[x - 1][y - 1], grid[x - 1][y + 1],
                           grid[x + 1][y + 1], grid[x + 1][y - 1]]
                if "".join(corners) in ["MMSS", "MSSM", "SSMM", "SMMS"]:
                    count += 1

    return count


if __name__ == "__main__":
    with open('input.txt', 'r') as word_search:
        grid = word_search.read().split()
        print(count_xmas_appearances(grid))
        print(count_x_mas_appearances(grid))
