from input import read_input_file, InputFile
import re

def day_three_part_one() -> int :
    inp: InputFile = read_input_file("input_files/day_three.txt")
    
    sum: int = 0
    for stmt in inp.lines:
        sum += compute(stmt)
    
    return sum


def compute(line: str) -> int:
    total = 0
    
    # Find all valid 'mul(X,Y)' expressions where X and Y are up to three digits
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)

    # Multiply the pairs and accumulate the sum
    for match in matches:
        x, y = map(int, match)  # Convert to integers
        total += x * y  # Add the result of multiplication to the total

    return total


def day_three_part_two() -> int:
    inp: InputFile = read_input_file("input_files/day_three.txt")
    
    total_sum = 0

    for stmt in inp.lines:
        # Split the string based on do() and don't() markers
        parts = re.split(r'(do\(\)|don\'t\(\))', stmt)
        mul_enabled = True  # Initially, `mul` instructions are enabled
        to_compute = []

        for part in parts:
            if part == "do()":
                mul_enabled = True
            elif part == "don't()":
                mul_enabled = False
            elif mul_enabled:
                # Extract valid mul() instructions from the current segment
                matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", part)
                to_compute.extend(matches)

        # Compute results for all valid instructions
        for expression in to_compute:
            total_sum += compute(expression)

    return total_sum