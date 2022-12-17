import csv
from UtilsGraph import UndirectedGraph as Graph
from UtilsGraph import DirectedGraph as DGraph
from UtilsGraph import WeightedEdge as Edge
from UtilsGraph import WeightedArc as Arc


def undirected_graph_data_loader(csv_filepath: str, skip: int = 0):
    graph = Graph([], [])
    with open(csv_filepath) as file:
        reader = csv.reader(file, delimiter=" ")
        header_row = next(reader)
        print("HEAD:", header_row)
        for row in reader:
            if skip != 0:
                skip = skip - 1
                continue
            graph.add_edge(Edge(set([int(row[0]), int(row[1])]), int(row[2])))

    return graph


def directed_graph_data_loader(csv_filepath: str, skip: int = 0) -> DGraph:
    graph = DGraph([], [])
    with open(csv_filepath) as file:
        reader = csv.reader(file, delimiter=" ")
        header_row = next(reader)
        print("HEAD:", header_row)
        for row in reader:
            if skip != 0:
                skip = skip - 1
                continue
            graph.add_arc(Arc(int(row[0]), int(row[1]), int(row[2])))

    return graph
