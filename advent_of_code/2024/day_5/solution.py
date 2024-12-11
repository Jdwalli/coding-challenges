
def is_good(orderings, updates: list) -> bool:
    map = {}
    for i, value in enumerate(updates):
        map[value] = i

    for a, b in orderings:
        if a in map and b in map and not map[a] < map[b]:
            print(a, b)
            return False
    return True

def calculate_middle_page_number(orderings: list, updates: list) -> int:
    count = 0
    for update in updates:
        if is_good(orderings, update):
            count += update[len(update) // 2]
    return count


def calculate_middle_page_number_after_fix(orderings: list, updates: list) -> int:
    count = 0
    return count
    

if __name__ == "__main__":
    with open('input.txt', 'r') as print_queue:
        data = print_queue.read().strip()
        parts = data.split("\n\n")
        orderings = [list(map(int, line.split('|'))) for line in parts[0].splitlines()]
        updates = [list(map(int, line.split(','))) for line in parts[1].splitlines()]
        print(calculate_middle_page_number(orderings, updates))
        # print(calculate_middle_page_number_after_fix(orderings, updates))
