
separator = '|'

def calculate_card_points(card):
    winning_values, elf_values = card.split(": ")[1].split(separator)
    winning_values = [int(n) for n in winning_values.split()]
    elf_values = [int(n) for n in elf_values.split()]
    matches = 0

    for value in elf_values:
        if value in winning_values:
            matches += 1

    return 2 ** (matches - 1) if matches > 0 else 0

def solve_part_one(scratchcard_data):
    score = 0
    for card in scratchcard_data:
        score += calculate_card_points(card)
    return score


def solve_part_two(scratchcard_data): 
    counts = [1] * len(scratchcard_data)
    for index, card in enumerate(scratchcard_data):
        winning_values, elf_values = card.split(": ")[1].split(separator)
        winning_values = [int(n) for n in winning_values.split()]
        elf_values = [int(n) for n in elf_values.split()]
        num_matches = len([c for c in elf_values if c in winning_values])
        first_index = index + 1
        for i in range(first_index, first_index + num_matches):
            counts[i] += counts[index]
    return sum(counts)


if __name__ == "__main__":
    with open('input.txt', 'r') as scratchcards:
        scratchcard_data = scratchcards.readlines()
        assert solve_part_one(scratchcard_data) == 21568
        assert solve_part_two(scratchcard_data) == 11827296
        print(solve_part_one(scratchcard_data))
        print(solve_part_two(scratchcard_data))