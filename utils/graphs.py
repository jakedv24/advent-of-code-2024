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

class Point:
    x: int
    y: int
    
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)
    
    def __hash__(self):
        # Hash based on the x and y values
        return hash((self.x, self.y))
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"