from functools import cache

@cache
def recursive_blinks(stone: int, remaining_blinks: int) -> int:
    if remaining_blinks == 0:
        return 1

    if stone == 0:
        return recursive_blinks(1, remaining_blinks - 1)

    stone_len = len(str(stone))

    if stone_len % 2 == 0:
        x = (int(str(stone)[:stone_len // 2]))
        y = (int(str(stone)[stone_len // 2:]))

        return recursive_blinks(x, remaining_blinks - 1) + recursive_blinks(y, remaining_blinks - 1)

    return recursive_blinks(stone * 2024, remaining_blinks - 1)


if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        data = list(map(int, file.readline().strip().split(" ")))
        print(sum([recursive_blinks(stone, 25) for stone in data]))
        print(sum([recursive_blinks(stone, 75) for stone in data]))
