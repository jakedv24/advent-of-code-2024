from utils.input import read_input_file, InputFile

class Equation:
    original: str
    target: int
    items: list[int]

    def __init__(self, line: str):
        self.original = line
        
        target, items = line.split(":")
        self.target = int(target)
        self.items = list(map(int, items.split()))
    
    def sum_of_items(self) -> int:
        return sum(self.items)
    


def day_seven_part_1():
    inp: InputFile = read_input_file("input_files/day_seven.txt")
    lines = inp.lines
    
    equations: list[Equation] = []
    for l in lines:
        equations.append(Equation(l))
    
    total_sum = 0
    for eq in equations:
        if target_is_possible(eq):
            total_sum += eq.target
    
    return total_sum


def day_seven_part_2():
    inp: InputFile = read_input_file("input_files/day_seven.txt")
    lines = inp.lines
    
    equations: list[Equation] = []
    for l in lines:
        equations.append(Equation(l))
    
    total_sum = 0
    for eq in equations:
        if target_is_possible(eq, True):
            total_sum += eq.target
    
    return total_sum


def target_is_possible(eq: Equation, or_operator = False) -> bool:
    return target_is_possible_recursive(eq.items[0], 1, eq.items, eq.target, or_operator)


def target_is_possible_recursive(current: int, i: int, numbers: list[int], target: int, or_operator: bool) -> bool:
    if i == len(numbers):
        return current == target
    elif current > target: # only add and multiple allowed
        return False
    
    add = target_is_possible_recursive(current + numbers[i], i + 1, numbers, target, or_operator)
    mult = target_is_possible_recursive(current * numbers[i], i + 1, numbers, target, or_operator)
    res = add or mult
    
    if or_operator:
        operation = int(str(current) + str(numbers[i]))
        res = res or target_is_possible_recursive(operation, i + 1, numbers, target, or_operator)
    
    return res