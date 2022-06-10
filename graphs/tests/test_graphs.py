"""
    
    
    
    
    
    
    
    
"""
from graphs.graph import Vertex, Graph
import pytest


def test_instantiate_graph():
    """[8] An empty graph properly returns null"""
    graph = Graph()
    actual = list(graph.get_nodes())
    expected = []
    assert actual == expected


def test_add_to_graph(get_graph):
    """[1] Node can be successfully added to the graph"""
    actual_before_add = get_graph.size()
    expected_before_add = 6
    assert actual_before_add == expected_before_add

    get_graph.add_node("ABC")
    actual = get_graph.size()
    expected = 7
    assert actual == expected


def test_get_neighbors(get_graph):
    """[2] An edge can be successfully added to the graph"""
    add_vertex = get_graph.add_node("H")
    actual = get_graph.get_neighbors(add_vertex)
    expected = []
    assert actual == expected


def test_get_all_nodes(get_graph):
    """[3] A collection of all nodes can be properly retrieved from the graph"""
    vertices = list(get_graph.get_nodes())
    expected = True
    for actual in vertices:
        assert isinstance(actual, Vertex) == expected


def test_retrieved_neighbors(get_graph):
    """[4] All appropriate neighbors can be retrieved from the graph"""
    keys = list(get_graph.get_nodes())
    actual = get_graph.get_neighbors(keys[0])
    expected = (keys[1], 0)
    assert actual[0].vertex == expected[0]


def test_neighbors_with_weight(get_graph):
    """[5] Neighbors are returned with the weight between nodes included"""
    keys = get_graph.get_nodes()
    first_vertex = list(keys)[0]
    neighbors = get_graph.get_neighbors(first_vertex)
    first_neighbor, second_neighbor = neighbors
    actual_first_neighbor_weight = first_neighbor.weight
    actual_first_neighbor_vertex_value = first_neighbor.vertex.value
    expected_first_neighbor_weight = 0
    expected_first_neighbor_vertex_value = "B"
    assert actual_first_neighbor_vertex_value == expected_first_neighbor_vertex_value
    assert actual_first_neighbor_weight == expected_first_neighbor_weight


def test_graph_size(get_graph):
    """[6] The proper size is returned, representing the number of nodes in the graph"""
    actual = get_graph.size()
    expected = 6
    assert actual == expected


def test_graph_with_one_node():
    """[7] A graph with only one node and edge can be properly returned"""
    graph = Graph()
    added_node = graph.add_node(["Hello", "world"])
    actual_neighbors = graph.get_neighbors(added_node)
    expected_neighbors = []
    actual = added_node.value
    expected = ["Hello", "world"]
    assert actual == expected

    assert actual_neighbors == expected_neighbors


@pytest.fixture
def get_graph():
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

    return graph
