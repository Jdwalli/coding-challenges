
def blink(input: list[int], remaining_blinks: int) -> list[int]:
    if remaining_blinks == 0:
        return input
    
    # Perform a single blink
    new_stones = []
    for stone in input:
        # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. 
            str_dig = str(stone)
            split_idx = len(str_dig) // 2
            #  The left half of the digits are engraved on the new left stone
            left = str_dig[:split_idx]
            #  right half of the digits are engraved on the new right stone
            right = str_dig[split_idx:]
            new_stones.append(int(left))
            new_stones.append(int(right))
        else:
            new_stones.append(2024 * stone)
    
    return blink(new_stones, remaining_blinks - 1)
    


if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        data = list(map(int, file.readline().strip().split(" ")))
        print(len(blink(data, 25)))