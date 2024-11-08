
def solve_part_one(race_data: str) -> int:
    data = race_data.split("\n")
    t = list(map(int, data[0].split(":")[1].split()))
    d = list(map(int, data[1].split(":")[1].split()))
    td_mapping = list(zip(t, d))
    sol = 1
    
    for mapping in td_mapping:
        win_count = 0
        rt, rd = mapping[0], mapping[1]
        for holding_possibility in range(0, rt + 1):
            if ((rt - holding_possibility) * holding_possibility) > rd:
                win_count += 1
        sol *= win_count
                
    return sol


def solve_part_two(race_data: str) -> int:
    data = race_data.split("\n")
    td_mapping = [
        (int(data[0].split(":")[1].replace(" ", '')), int(data[1].split(":")[1].replace(" ", '')))
    ]

    sol = 1
    
    for mapping in td_mapping:
        win_count = 0
        rt, rd = mapping[0], mapping[1]
        for holding_possibility in range(0, rt + 1):
            if ((rt - holding_possibility) * holding_possibility) > rd:
                win_count += 1
        sol *= win_count
                
    return sol


if __name__ == "__main__":
    with open('input.txt', 'r') as race_paper:
        race_data = race_paper.read()
        assert solve_part_one(race_data) == 220320
        assert solve_part_two(race_data) == 34454850
        print(solve_part_one(race_data))
        print(solve_part_two(race_data))
