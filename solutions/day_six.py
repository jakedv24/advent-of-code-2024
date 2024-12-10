import copy
import pprint

from utils.input import read_input_file, InputFile
from utils.graphs import point_in_bounds, add_tuples, find_element

dirs = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]

dirCodes = [
    "U",
    "R",
    "D",
    "L"
]

def dir_codes_with_wraparound(i: int) -> str:
    return dirCodes[i % len(dirCodes)]


def dir_with_wraparound(i: int) -> tuple[int, int]:
    return dirs[i % len(dirs)]

def day_six_part_1():
    inp: InputFile = read_input_file("input_files/day_six.txt")
    graph = inp.lines
    graph = list(map(lambda s: list(s), graph))
    
    # find guard
    x, y = find_element(graph, "^")
    distinct_points, _ = traverse_graph(x, y, graph)
    
    print(len(distinct_points))

def day_six_part_2():
    inp: InputFile = read_input_file("input_files/day_six.txt")
    graph = inp.lines
    graph = list(map(lambda s: list(s), graph))
    
    # find guard
    x, y = find_element(graph, "^")
    # get all possible points of a blockade
    distinct_points, _ = traverse_graph(x, y, copy.deepcopy(graph))
    
    num_loops = 0
    for i, pt in enumerate(distinct_points[1:]):
        # put block at point and see if it gets a loop
        new_graph = copy.deepcopy(graph)
        new_graph[pt[0]][pt[1]] = "#"
        _, loop = traverse_graph(x, y, new_graph)
        
        if loop:
            num_loops += 1
            
        print(f"looping i: {i}, pt: {pt}, num loops: {num_loops}")
    
    print(num_loops)


def traverse_graph(x: int, y: int, graph: list[list[str]]) -> tuple[list[tuple[int, int]], bool]:
    dir = dirs[0]
    dirC = dirCodes[0]
    dirI = 0
    
    distinct_points: list[tuple[int, int]] = [(x, y)]
    graph[x][y] = dirC
    
    while(point_in_bounds((x, y), graph)):
        # move or turn
        next = add_tuples(dir, (x, y))
        if not point_in_bounds(next, graph):
            break
        nextX, nextY = next[0], next[1]
        
        if graph[nextX][nextY] == "#":
            # turn right
            dirI += 1
            dir = dir_with_wraparound(dirI)
            dirC = dir_codes_with_wraparound(dirI)
        elif graph[next[0]][next[1]] == dirC:
            # loop?
            return distinct_points, True
        else:
            # move, mark if not already
            x = next[0]
            y = next[1]
            
            if graph[x][y] == ".":
                distinct_points.append((x, y))
            
            graph[x][y] = dirC
    
    return distinct_points, False