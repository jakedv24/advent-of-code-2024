from utils.input import read_input_file, InputFile
from utils.graphs import Point, point_in_bounds

def day_eight_part_1():
    inp: InputFile = read_input_file("input_files/day_eight.txt")
    graph = inp.graph()
    
    freqToAntennas = scan_graph_for_antennas(inp.graph())
    antinodes: set[Point] = set()
    
    for _, antennas in freqToAntennas.items():
        for ant in antennas:
            for otherAnt in antennas:
                if ant == otherAnt:
                    continue
                
                dist = otherAnt - ant
                move = dist * Point(-1, -1)
                antinode = ant + move
                
                if point_in_bounds((antinode.x, antinode.y), inp.graph()):
                    antinodes.add(antinode)
                    graph[antinode.x][antinode.y] = "#"
                    
    
    return len(antinodes)


def day_eight_part_2():
    inp: InputFile = read_input_file("input_files/day_eight.txt")
    graph = inp.graph()
    
    freqToAntennas = scan_graph_for_antennas(inp.graph())
    antinodes: set[Point] = set()
    
    for _, antennas in freqToAntennas.items():
        for ant in antennas:
            for otherAnt in antennas:
                if ant == otherAnt:
                    continue
                
                dist = otherAnt - ant
                move = dist * Point(-1, -1)
                antinode = ant
                while(point_in_bounds((antinode.x, antinode.y), inp.graph())):
                    antinodes.add(antinode)
                    graph[antinode.x][antinode.y] = "#"
                    antinode = antinode + move
                    
    
    return len(antinodes)


def scan_graph_for_antennas(graph: list[list[str]]) -> dict[str, set[Point]]:
    freqToAntennas: dict[str, set[Point]] = {}
    for x, row in enumerate(graph):
        for y, char in enumerate(row):
            if char != "." and char != "\n":
                freqToAntennas.setdefault(char, set()).add(Point(x, y))
    
    return freqToAntennas