from collections import deque
from copy import deepcopy

from utils.graphs import Point, point_in_bounds, point_obj_in_bounds
from utils.input import read_input_file, InputFile

def day_ten_part_1():
    inp: InputFile = read_input_file("input_files/day_ten.txt")
    graph = inp.graph()
    trailheads = find_trailheads(graph)
    
    sum = 0
    for th in trailheads:
        sum += bfs_trailhead(th, graph)
    
    return sum


def day_ten_part_2():
    inp: InputFile = read_input_file("input_files/day_ten.txt")
    graph = inp.graph()
    trailheads = find_trailheads(graph)
    
    sum = 0
    for th in trailheads:
        sum += bfs_trailhead(th, graph, True)
    
    return sum


def find_trailheads(graph: list[list[str]]) -> list[Point]:
    points: list[Point] = []
    
    for i, row in enumerate(graph):
        for j, c in enumerate(row):
            if c ==  "0":
                points.append(Point(i, j))
                
    return points


def bfs_trailhead(start: Point, g: list[list[str]], rating = False) -> int:
    trail_score = 0
    graph = deepcopy(g)
    queue: deque[Point] = deque()
    queue.append(start)
    
    while(len(queue) > 0):
        curr = queue.popleft()
        
        if not point_obj_in_bounds(curr, graph) or point_visited(curr, graph):
            continue
                
        # if we are at a peak, increase score
        if height_at_point(curr, graph) == 9:
            trail_score += 1
        
        for n in curr.neighbors():
            # only append the neighbor if it meets req. In bounds, not visited, increase by 1.
            if point_obj_in_bounds(n, graph) and not point_visited(n, graph) and (height_at_point(n, graph) - height_at_point(curr, graph) == 1):
                queue.append(n)

        if not rating:
            mark_point_visited(curr, graph)
    
    return trail_score


def height_at_point(p: Point, graph: list[list[str]]) -> int:
    return int(graph[p.x][p.y])

def mark_point_visited(p: Point, graph: list[list[str]]):
    graph[p.x][p.y] = "."

def point_visited(p: Point, graph: list[list[str]]) -> bool:
    return graph[p.x][p.y] == "."