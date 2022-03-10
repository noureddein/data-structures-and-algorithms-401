import pytest
from linked_lists.linked_list import LinkedList
from linked_lists.node import Node


# @pytest.mark.skip("todo")
def test_empty_list():
    # ?[1] Can successfully instantiate an empty linked list
    ll = LinkedList()
    actual = ll.head
    expected = None
    assert actual == expected


def test_inserting(one_node):
    # ?[2] Can properly insert into the linked list
    actual = one_node.includes('A')
    expected = True

    assert actual == expected


def test_head_point_to_first_node(one_node):
    # ?[3] The head property will properly point to the first node in the linked list
    actual = one_node.head.value
    expected = 'A'

    assert actual == expected


def test_insert_multiple_nodes(ll):
    # ?[4] Can properly insert multiple nodes into the linked list
    ll.insert(Node([1, 2, 3]))
    actual = ll.includes([1, 2, 3])
    expected = True
    assert actual == expected

    ll.insert(Node('Hello'))
    actual = ll.includes('Hello')
    expected = True
    assert actual == expected

    obj = {
        "name": "Nirvana",
        "members": [
            {"name": "Kurt Cobain", "instrument": "Guitar"},
            {"name": "Krist Novoselic", "instrument": "Bass"},
            {"name": "Dave Grohl", "instrument": "Drums"},
        ],
    }
    ll.insert(Node(obj))
    actual = ll.includes(obj)
    expected = True
    assert actual == expected


def test_finding_values(multiple_nodes):
    # ?[5] Will return true when finding a value within the linked list that exists
    actual = multiple_nodes.includes('A')
    expected = True
    assert actual == expected

    actual = multiple_nodes.includes('B')
    expected = True
    assert actual == expected

    actual = multiple_nodes.includes('C')
    expected = True
    assert actual == expected

    actual = multiple_nodes.includes('D')
    expected = True
    assert actual == expected


def test_not_exist(multiple_nodes):
    # ?[6] Will return false when searching for a value in the linked list that does not exist
    actual = multiple_nodes.includes("E")
    expected = False

    assert actual == expected


def test_return_collection_of_values(multiple_nodes):
    # ?[7] Can properly return a collection of all the values that exist in the linked list
    actual = multiple_nodes.to_string()
    expected = '{ D } -> { C } -> { B } -> { A } -> Null'
    assert actual == expected


@pytest.fixture
def ll():
    ll = LinkedList()
    return ll


@pytest.fixture
def one_node():
    first_node = LinkedList()
    first_node.insert(Node('A'))
    return first_node


@pytest.fixture
def multiple_nodes():
    nodes = LinkedList()
    nodes.insert(Node('A'))
    nodes.insert(Node('B'))
    nodes.insert(Node('C'))
    nodes.insert(Node('D'))
    return nodes
