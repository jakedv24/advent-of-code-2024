def point_in_bounds(point: tuple[int, int], graph: list[str]) -> bool:
    x, y = point
    return x > -1 and y > -1 and x < len(graph) and y < len(graph[0])