from solutions.day_eight import scan_graph_for_antennas, day_eight_part_1, day_eight_part_2
from utils.graphs import Point

def test_scan_graph():
    graph = [
        [".", ".", "a"],
        ["a", ".", "b"]
    ]
    
    assert scan_graph_for_antennas(graph) == {
        "a": set([Point(0, 2), Point(1, 0)]),
        "b": set([Point(1, 2)])
    }


def test_part_one():
    graph = [
        [".", ".", "a"],
        ["a", ".", "b"]
    ]
    
    assert scan_graph_for_antennas(graph) == {
        "a": set([Point(0, 2), Point(1, 0)]),
        "b": set([Point(1, 2)])
    }


def test_part_one_input():
    assert day_eight_part_1() == 367

def test_part_two():
    assert day_eight_part_2() == 1285