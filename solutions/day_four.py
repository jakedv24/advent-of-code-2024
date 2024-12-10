from input import InputFile, read_input_file
from graphs import point_in_bounds, add_tuples, negate_tuple

keyword = "XMAS"

def day4part1():
    inp = read_input_file("input_files/day_four.txt")
    lines = inp.lines
    
    sum = 0
    for x, line in enumerate(lines):
        for y, _ in enumerate(line):
            sum += check_keyword(keyword, x, y, lines)
    
    print(sum)


def day4part2():
    inp = read_input_file("input_files/day_four.txt")
    lines = inp.lines
    
    sum = 0
    for x, line in enumerate(lines):
        for y, _ in enumerate(line):
            if lines[x][y] == 'A':
                # top left and top right corners
                dirs = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
                numMatches = 0
                for dir in dirs:
                    point: tuple[int, int] = add_tuples((x, y), negate_tuple(dir))
                    
                    if check_direction("MAS", point[0], point[1], dir, lines):
                        numMatches += 1
                
                if numMatches == 2:
                    sum += 1
    
    print(sum)


# check if a keyword starts at this point
def check_keyword(keyword: str, x: int, y: int, lines: list[str]) -> int:
    # check first char is indeed the starting char
    if lines[x][y] != keyword[0]:
        return False
    
    # check if surrounding chars are the second char
    # if they are, continue in that direction to determine full word
    dirs: list[tuple[int, int]] = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]
    point: tuple[int, int] = (x, y)
    
    matches_from_source: int = 0
    for dir in dirs:
        # check the word full in that dir
        if check_direction(keyword, x, y, dir, lines):
            matches_from_source += 1
    
    return matches_from_source


# follows a certain direction until boundary or complete word is found, breaks out otherwise
def check_direction(keyword: str, startX: int, startY: int, dir: tuple[int, int], graph: list[str]) -> bool:
    point: tuple[int, int] = (startX, startY)
    for c in keyword:
        if not point_in_bounds(point, graph) or c != graph[point[0]][point[1]]:
            return False
        
        # move in direction
        point = add_tuples(point, dir)
    
    return True