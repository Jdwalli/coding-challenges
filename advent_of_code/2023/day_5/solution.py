def solve_part_one(almanac_data: str) -> int:
    seeds, *blocks = almanac_data.split("\n\n")
    # Assigns first values to seeds and rest to blocks
    seeds = list(map(int, seeds.split(":")[1].split()))

    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        new = []

        for x in seeds:
            for a, b, c in ranges:
                if x in range(b, b + c):
                    new.append(x - b + a)
                    break
            else:
                new.append(x)
        seeds = new

    return min(seeds)


def solve_part_two(almanac_data: str) -> int:
    inputs, *blocks = almanac_data.split("\n\n")
    # Assigns first values to seeds and rest to blocks
    inputs = list(map(int, inputs.split(":")[1].split()))

    seeds = []

    for i in range(0, len(inputs), 2):
        seeds.append((inputs[i], inputs[i] + inputs[i + 1]))

    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        new = []

        while len(seeds) > 0:
            start, end = seeds.pop()
            for a, b, c in ranges:
                overlap_start = max(start, b)
                overlap_end = min(end, b + c)
                if overlap_start < overlap_end:
                    new.append((overlap_start - b + a, overlap_end - b + a))
                    if overlap_start > start:
                        seeds.append((start, overlap_start))
                    if end > overlap_end:
                        seeds.append((overlap_end, end))
                    break
            else:
                new.append((start, end))
        seeds = new

    return (min(seeds)[0])


if __name__ == "__main__":
    with open('input.txt', 'r') as almanac:
        almanac_data = almanac.read()
        assert solve_part_one(almanac_data) == 379811651
        assert solve_part_two(almanac_data) == 27992443
        print(solve_part_one(almanac_data))
        print(solve_part_two(almanac_data))
