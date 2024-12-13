from solutions.day_ten import bfs_trailhead, find_trailheads
from utils.graphs import Point


test_graph: list[list[str]] = [
    ["8", "9", "0", "1", "0", "1", "2", "3"],
    ["7", "8", "1", "2", "1", "8", "7", "4"],
    ["8", "7", "4", "3", "0", "9", "6", "5"], 
    ["9", "6", "5", "4", "9", "8", "7", "4"],
    ["4", "5", "6", "7", "8", "9", "0", "3"],
    ["3", "2", "0", "1", "9", "0", "1", "2"],
    ["0", "1", "3", "2", "9", "8", "0", "1"],
    ["1", "0", "4", "5", "6", "7", "3", "2"]
]

def test_find_trailhead():
    assert len(find_trailheads(test_graph)) == 9


def test_bfs_trailhead():
    th = Point(0, 2)
    assert(bfs_trailhead(th, test_graph)) == 5
    
    th = Point(0, 4)
    assert(bfs_trailhead(th, test_graph)) == 6
    
    th = Point(2, 4)
    assert(bfs_trailhead(th, test_graph)) == 5
    
    th = Point(0, 2)
    assert(bfs_trailhead(th, test_graph, True)) == 20