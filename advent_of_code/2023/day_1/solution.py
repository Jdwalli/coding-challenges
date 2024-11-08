import regex

def solve_part_one(calibration_data: list[str]) -> int:
    values = 0
    for calibration in calibration_data:
        data = calibration.strip()
        numbers = []
        for element in data:
            if element.isdigit():
                numbers.append(element)
        values += int(f"{numbers[0]}{numbers[-1]}")
    return values

def solve_part_two(calibration_data: list[str]) -> int:
    digits = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    values = 0

    for data in calibration_data:
        data = data.strip()
        numbers = regex.findall(
            f"(\d|{'|'.join(digits.keys())})", data, overlapped=True)
        
        if numbers[0] in digits:
            numbers[0] = digits[numbers[0]]
        if numbers[-1] in digits:
            numbers[-1] = digits[numbers[-1]]

        values += int(f"{numbers[0]}{numbers[-1]}")
    return values


if __name__ == "__main__":
    with open('input.txt', 'r') as calibration_file:
        calibration_data = calibration_file.readlines()
        print(f"Part One: {solve_part_one(calibration_data)}")
        print(f"Part Two: {solve_part_two(calibration_data)}")