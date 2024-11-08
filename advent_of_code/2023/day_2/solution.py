import re

def solve_part_one(cube_game_data: list[str]) -> int:
    value = 0
    full_game_breakdown = []

    for cube_game in cube_game_data:
        game_breakdown = {'id': re.search(r"^Game\s+(\d+):", cube_game).group(1)}

        matches = re.findall(r'(\d+)\s*(\w+)', cube_game)
        validty = [int(count) <= 12 if color == 'red' else int(count) <= 13 if color == 'green' else int(count) <= 14 for count, color in matches]

        game_breakdown['valid'] = validty
        full_game_breakdown.append(game_breakdown)
    
    value = sum(int(element['id']) for element in full_game_breakdown if all(element['valid']))

    return value


def solve_part_two(cube_game_data: list[str]) -> int:
    powers = []

    for cube_game in cube_game_data:
        max_values = {'red': 0, 'green': 0, 'blue': 0}
        matches = re.findall(r'(\d+)\s*(\w+)', cube_game)

        for element in matches:
            color = element[1]
            value = int(element[0])

            if value > max_values.get(color, 0):
                max_values[color] = value

        
        powers.append(max_values['red'] * max_values['green'] * max_values['blue'])

    return sum(powers)


if __name__ == "__main__":
    with open('input.txt', 'r') as cube_game_file:
        cube_game_data = cube_game_file.readlines()
        print(solve_part_one(cube_game_data))
        print(solve_part_two(cube_game_data))