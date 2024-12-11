
def create_block(input: str) -> list:
    block = ""
    id = 0
    for index in range(len(input)): # 0 index, if odd its a space
        if index % 2 == 0:
           block += (str(id) * int(input[index]))
           id += 1
        else:
            block += ("." * int(input[index]))
    return list(block)

def move_file_blocks(input: str) -> list:
    block = create_block(input)
    blank_space = [i for i, x in enumerate(block) if x == "."]
    for idx in blank_space:
        while block[-1] == '.': 
            block.pop()
        if len(block) <= idx: 
            break
        block[idx] = block.pop()
    return block


def calculate_filesystem_checksum(input: str) -> int:
    return sum(i * int(x) for i, x in enumerate(move_file_blocks(input)))


if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        data = file.readline().strip()
        print(calculate_filesystem_checksum(data))