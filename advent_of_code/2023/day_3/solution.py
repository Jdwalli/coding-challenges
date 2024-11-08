
def get_adjacent_values(engine_schematic, row, col):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1), (1, 0), (1, 1)]

        adjacent_values = []

        for diagrow, diagcol in directions:
            new_row, new_col = row + diagrow, col + diagcol

            if 0 <= new_row < len(engine_schematic) and 0 <= new_col < len(engine_schematic[0]):
                if engine_schematic[new_row][new_col] != '.':
                    adjacent_values.append((new_row, new_col))
        return adjacent_values

def build_digit(engine_schematic, row, col):
    build = []
    row_length = len(engine_schematic[row])
    start = engine_schematic[row][col]
    build.append(start)


    # Right pointer
    current_col = col + 1 
    while current_col < row_length and engine_schematic[row][current_col] not in '.+-*/#$@=%&':
        build.append(engine_schematic[row][current_col])
        current_col += 1
    
    # Left pointer
    current_col = col - 1
    while current_col >= 0 and engine_schematic[row][current_col] not in '.+-*/#$@=%&':
        build.insert(0, engine_schematic[row][current_col])
        current_col -= 1

    return int(''.join(build))

def filter_adjacent_positions(list_of_lists):
    filtered_lists = list_of_lists

    for first_index, positions in enumerate(list_of_lists):
        for second_index, position in enumerate(positions):
            row, col = position
            left_position = (row, col - 1)
            right_position = (row, col + 1)

            if right_position in filtered_lists[first_index]:
                del filtered_lists[first_index][second_index]

            if left_position in filtered_lists[first_index]:
                del filtered_lists[first_index][second_index]

    return filtered_lists

def solve_part_one(engine_schematic):
    solution = 0
    target_symbols =  ["+", "-", "*", "/", "#", "$", "@", "=", "%", "&"]
    target_positions = []

    for row, engine_row in enumerate(engine_schematic):
        for col, engine_char in enumerate(engine_row):
            if engine_char in target_symbols:
                target_positions.append(get_adjacent_values(engine_schematic, row, col))


    target_positions = filter_adjacent_positions(target_positions)

    for symbol_entry in target_positions:
        for position in symbol_entry:
            if position:
                solution += build_digit(engine_schematic, position[0], position[1])
            
    return solution


def solve_part_two(engine_schematic):
    solution = 0
    target_symbols =  ["*"]
    target_positions = []
    for row, engine_row in enumerate(engine_schematic):
        for col, engine_char in enumerate(engine_row):
            if engine_char in target_symbols:
                target_positions.append(get_adjacent_values(engine_schematic, row, col))
    
    target_positions = filter_adjacent_positions(target_positions)

    for gear_positions in target_positions:
        if len(gear_positions) == 2:
            ratio_one = build_digit(engine_schematic,gear_positions[0][0], gear_positions[0][1])
            ratio_two = (build_digit(engine_schematic,gear_positions[1][0], gear_positions[1][1]))
            solution += (ratio_one * ratio_two)  

    return solution       


if __name__ == "__main__":
    with open('input.txt', 'r') as engine_schematic_file:
        engine_schematic_data = engine_schematic_file.readlines()
        print(solve_part_one(engine_schematic_data))
        print(solve_part_two(engine_schematic_data))
