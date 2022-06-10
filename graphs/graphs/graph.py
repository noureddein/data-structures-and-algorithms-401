class CustomError(Exception):
    pass


class Vertex:
    def __init__(self, value):
        self.value = value

    # def __str__(self) -> str:
    #     return str(self.value)

    # def __repr__(self) -> str:
    #     return str(self.value)


class Edge:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight

    # def __str__(self) -> str:
    #     return str(f"({self.vertex}, {self.weight})")

    # def __repr__(self) -> str:
    #     return str(f"({self.vertex}, {self.weight})")


class Graph:
    def __init__(self) -> None:
        self.__adjacency_list = {}

    def add_node(self, value):
        """

        add new node

        Arguments: value

        Returns: The added node

        Add a node to the graph

        """
        new_node = Vertex(value)
        self.__adjacency_list[new_node] = []
        return new_node

    def add_edge(self, start_vertex, end_vertex, weight=0):
        """
        Arguments: 2 nodes to be connected by the edge, weight (optional)

        Returns: nothing

        Adds a new edge between two nodes in the graph

        If specified, assign a weight to the edge

        Both nodes should already be in the Graph

        """
        if not isinstance(start_vertex, Vertex) or not isinstance(end_vertex, Vertex):
            raise CustomError(
                "Your 'start_vertex' argument is not an instance of Vertex class."
            )

        edge = Edge(end_vertex, weight)
        self.__adjacency_list[start_vertex].append(edge)

    def get_nodes(self):
        """
        Arguments: none
        Returns all of the nodes in the graph as a collection (set, list, or similar)
        """
        return self.__adjacency_list.keys()

    def get_neighbors(self, vertex):
        """
        get neighbors
        Arguments: node
        Returns a collection of edges connected to the given node
        Include the weight of the connection in the returned collection
        """
        return self.__adjacency_list.get(vertex, [])

    def size(self):
        """
        Arguments: none
        Returns the total number of nodes in the graph
        """
        return len(self.__adjacency_list)

    def print_graph(self):
        """Print the adjacency list."""
        return self.__adjacency_list

    def __repr__(self) -> str:
        return str(self.__adjacency_list)


if __name__ == "__main__":

    graph = Graph()
    a = graph.add_node("A")
    b = graph.add_node("B")
    c = graph.add_node("C")
    d = graph.add_node("D")
    e = graph.add_node("E")
    f = graph.add_node("F")

    graph.add_edge(a, b)
    graph.add_edge(a, c)
    graph.add_edge(b, d)
    graph.add_edge(c, e)
    graph.add_edge(d, f)

    print(graph.print_graph())
