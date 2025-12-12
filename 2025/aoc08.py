import math
from collections import Counter
from functools import reduce

class Graph:

    def __init__(self):
        self.points = []

    def add_point(self, point):
        self.points.append(point)

class Aoc:

    def __init__(self, input):
        coords = []
        for line in input:
            x,y,z = list(map(int, line.split(",")))
            coords.append((x,y,z))
        self.input = coords

    def part_one(self, limit=10):
        coords = self.input[:]
        # get all the distances which to sort by later to get the top x connections
        distances = []
        for i in range(len(coords)):
            for x in range(len(coords)):
                if x > i:
                    distance = self.get_distance(coords[i], coords[x])
                    distances.append((distance, i,x))
        distances.sort()

        # if none of the points are in a graph, make a new graph with them, if one is, add the other to the same graph, if both are, ignore
        parents = {}
        for i in range(limit):
            _, a,b = distances[i]
            if a in parents:
                a_graph = parents[a]
                if b in parents:
                    b_graph = parents[b]
                    if a_graph != b_graph:
                        for val in b_graph.points:
                            a_graph.add_point(val)
                            parents[val] = a_graph
                else:
                    a_graph.add_point(b)
                    parents[b] = a_graph
            elif b in parents:
                b_graph = parents[b]
                if a in parents:
                    a_graph = parents[a]
                    if a_graph != b_graph:
                        for val in a_graph.points:
                            b_graph.add_point(val)
                            parents[val] = b_graph
                else:
                    b_graph.add_point(a)
                    parents[a] = b_graph
            else:
                graph = Graph()
                graph.add_point(a)
                graph.add_point(b)
                parents[a] = graph
                parents[b] = graph
        graphs = set(list(parents.values()))
        connections = []
        for graph in graphs:
            connections.append(len(graph.points))
        connections.sort(reverse=True)
        return reduce(lambda x,y: x*y, connections[:3])

    def part_two(self):
        coords = self.input[:]
        # get all the distances which to sort by later to get the top x connections
        distances = []
        for i in range(len(coords)):
            for x in range(len(coords)):
                if x > i:
                    distance = self.get_distance(coords[i], coords[x])
                    distances.append((distance, i,x))
        distances.sort()

        # if none of the points are in a graph, make a new graph with them, if one is, add the other to the same graph, if both are, ignore
        parents = {}
        for i in range(len(distances)):
            _, a,b = distances[i]
            if a in parents:
                a_graph = parents[a]
                if b in parents:
                    b_graph = parents[b]
                    if a_graph != b_graph:
                        for val in b_graph.points:
                            a_graph.add_point(val)
                            parents[val] = a_graph
                        if len(a_graph.points) >= len(coords):
                            return coords[a][0] * coords[b][0]
                else:
                    a_graph.add_point(b)
                    parents[b] = a_graph
                    if len(a_graph.points) >= len(coords):
                        return coords[a][0] * coords[b][0]
            elif b in parents:
                b_graph = parents[b]
                if a in parents:
                    a_graph = parents[a]
                    if a_graph != b_graph:
                        for val in a_graph.points:
                            b_graph.add_point(val)
                            parents[val] = b_graph
                        if len(b_graph.points) >= len(coords):
                            return coords[a][0] * coords[b][0]
                else:
                    b_graph.add_point(a)
                    parents[a] = b_graph
                    if len(b_graph.points) >= len(coords):
                        return coords[a][0] * coords[b][0]
            else:
                graph = Graph()
                graph.add_point(a)
                graph.add_point(b)
                parents[a] = graph
                parents[b] = graph
        graphs = set(list(parents.values()))
        connections = []
        for graph in graphs:
            connections.append(len(graph.points))
        connections.sort(reverse=True)
        return None


    def get_distance(self,point_a, point_b):
        return math.sqrt((point_a[0]-point_b[0])**2 + (point_a[1] -point_b[1])**2 + (point_a[2] - point_b[2])**2)



test_file = "2025\\test_inputs\\aoc08.txt"
test_answer_a = 40
test_answer_b = 25272
run_file = "2025\\inputs\\aoc08.txt"

input = None
with open(test_file) as input_file:
    input = input_file.readlines()

test_aoc = Aoc(input)
test = test_aoc.part_one(limit=10)
assert(test_answer_a == test)

with open(run_file) as input_file:
    input = input_file.readlines()

run_aoc = Aoc(input)
answer = run_aoc.part_one(limit=1000)


test = test_aoc.part_two()
assert(test_answer_b == test)

answer = run_aoc.part_two()
print(answer)