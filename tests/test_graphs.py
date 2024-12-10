import graphs

def test_point_in_bounds():
    graph = [
        ["a", "b", "c"]
    ]
    
    invalid_points = [(-1, -1), (-1, 0), (4, 0), (0, 4), (0, -1)]
    valid_points = [(0, 1), (0, 0), (0, 2)]
    
    for inv in invalid_points:
        assert graphs.point_in_bounds(inv, graph) == False
        
    for val in valid_points:
        assert graphs.point_in_bounds(val, graph) == True


def test_add_tuples():
    assert graphs.add_tuples((0, 1), (1, 0)) == (1, 1)
    assert graphs.add_tuples((-1, -1), (-1, -1)) == (-2, -2)


def test_negate_tuple():
    assert graphs.negate_tuple((0, 1)) == (0, -1)
    assert graphs.negate_tuple((1, 1)) == (-1, -1)
    assert graphs.negate_tuple((-1, -1)) == (1, 1)


def test_find_element():
    graph = [
        ["a", "b", "c"]
    ]
    
    assert graphs.find_element(graph, "c") == (0, 2)
    assert graphs.find_element(graph, "a") == (0, 0)
    assert graphs.find_element(graph, "b") == (0, 1)