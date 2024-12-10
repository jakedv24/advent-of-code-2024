def point_in_bounds(point: tuple[int, int], graph: list[list[str]]) -> bool:
    x, y = point
    return x > -1 and y > -1 and x < len(graph) and y < len(graph[0])

def add_tuples(one: tuple, two: tuple) -> tuple:
    return tuple(map(lambda i, j: i + j, one, two))

def negate_tuple(tup: tuple) -> tuple:
    return tuple(-x for x in tup)

def find_element(graph, element: str) -> tuple[int, int]:
    for i, _ in enumerate(graph):
        for j, c in enumerate(graph[i]):
            if c == element:
                return i, j
    
    return -1, -1