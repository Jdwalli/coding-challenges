
import re
from functools import reduce

def scan_basic_memory(memories: list):
    sol = 0
    for memory in memories:
        for x, y in re.findall(r"mul\((\d+),(\d+)\)", memory):
            sol += int(x) * int(y)
    return sol

def scan_memory_with_conditions(memory: str):
    sol = 0
    
    instructions = re.findall(r'(mul\(\d+,\d+\)|don\'t\(\)|do\(\))', memory)
    enabled = True
    for el in instructions:
        val = 0
        if el == "don't()":
            enabled = False
        elif el == "do()":
            enabled = True
        elif enabled:
            val = reduce(lambda x, y: x * y, map(int, re.findall(r'\d+', el)))
        sol += val

    return sol


if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        print(scan_basic_memory(file.readlines()))
        file.seek(0)
        print(scan_memory_with_conditions(file.read().strip()))
