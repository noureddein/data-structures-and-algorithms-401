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
    actual = one_node.includes("A")
    expected = True

    assert actual == expected


def test_head_point_to_first_node(one_node):
    # ?[3] The head property will properly point to the first node in the linked list
    actual = one_node.head.value
    expected = "A"

    assert actual == expected


def test_insert_multiple_nodes(ll):
    # ?[4] Can properly insert multiple nodes into the linked list
    ll.insert(Node([1, 2, 3]))
    actual = ll.includes([1, 2, 3])
    expected = True
    assert actual == expected

    ll.insert(Node("Hello"))
    actual = ll.includes("Hello")
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
    actual = multiple_nodes.includes("A")
    expected = True
    assert actual == expected

    actual = multiple_nodes.includes("B")
    expected = True
    assert actual == expected

    actual = multiple_nodes.includes("C")
    expected = True
    assert actual == expected

    actual = multiple_nodes.includes("D")
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
    expected = "{ D } -> { C } -> { B } -> { A } -> Null"
    assert actual == expected


def test_add_node_to_the_end(multiple_nodes):
    # ? [1] Can successfully add a node to the end of the linked list
    multiple_nodes.append(Node("F"))

    actual = multiple_nodes.to_string()
    expected = "{ D } -> { C } -> { B } -> { A } -> { F } -> Null"
    assert actual == expected

    actual = multiple_nodes.includes("F")
    expected = True
    assert actual == expected


def test_multiple_nodes_to_end_of_linked_list(multiple_nodes):
    # ? [2] Can successfully add multiple nodes to the end of a linked list
    multiple_nodes.append(Node("F"))
    multiple_nodes.append(Node("H"))
    multiple_nodes.append(Node("J"))

    actual = multiple_nodes.to_string()
    expected = "{ D } -> { C } -> { B } -> { A } -> { F } -> { H } -> { J } -> Null"
    assert actual == expected

    actual = multiple_nodes.includes("F")
    expected = True
    assert actual == expected

    actual = multiple_nodes.includes("H")
    expected = True
    assert actual == expected

    actual = multiple_nodes.includes("J")
    expected = True
    assert actual == expected


def test_insert_before_at_middle(multiple_nodes):
    # ?[3] Can successfully insert a node before a node located i the middle of a linked list

    actual = multiple_nodes.to_string()
    expected = "{ D } -> { C } -> { B } -> { A } -> Null"
    assert actual == expected

    multiple_nodes.insert_before("B", Node("F"))
    actual = multiple_nodes.to_string()
    expected = "{ D } -> { C } -> { F } -> { B } -> { A } -> Null"
    assert actual == expected


def test_insert_before_first_node(multiple_nodes):
    # ?[4] Can successfully insert a node before the first node of a linked list

    actual = multiple_nodes.to_string()
    expected = "{ D } -> { C } -> { B } -> { A } -> Null"
    assert actual == expected

    multiple_nodes.insert_before("D", Node("F"))
    actual = multiple_nodes.to_string()
    expected = "{ F } -> { D } -> { C } -> { B } -> { A } -> Null"
    assert actual == expected


def test_insert_after_node(multiple_nodes):
    # ?[5] Can successfully insert after a node in the middle of the linked list
    actual = multiple_nodes.to_string()
    expected = "{ D } -> { C } -> { B } -> { A } -> Null"
    assert actual == expected

    multiple_nodes.insert_after("C", Node("Hello World"))
    actual = multiple_nodes.to_string()
    expected = "{ D } -> { C } -> { Hello World } -> { B } -> { A } -> Null"
    assert actual == expected


def test_insert_after_last_node(multiple_nodes):
    # ?[6] Can successfully insert a node after the last node of the linked list

    actual = multiple_nodes.to_string()
    expected = "{ D } -> { C } -> { B } -> { A } -> Null"
    assert actual == expected

    multiple_nodes.insert_after("A", Node("Hello World"))
    actual = multiple_nodes.to_string()
    expected = "{ D } -> { C } -> { B } -> { A } -> { Hello World } -> Null"
    assert actual == expected


def test_delete_node(multiple_nodes):
    # Stretch Goal (Delete Node)

    # Delete from the beginning
    actual = multiple_nodes.includes("D")
    expected = True
    assert actual == expected

    actual = multiple_nodes.delete_node("D")
    expected = None
    assert actual == expected

    actual = multiple_nodes.includes("D")
    expected = False
    assert actual == expected

    # Delete the last node
    actual = multiple_nodes.includes("A")
    expected = True
    assert actual == expected

    actual = multiple_nodes.delete_node("A")
    expected = None
    assert actual == expected

    actual = multiple_nodes.includes("A")
    expected = False
    assert actual == expected


def test_k_equals_ll_length(multiple_nodes):
    # ?[1]  Where k and the length of the list are the same
    k = 4
    actual = multiple_nodes.get_ll_length()
    expected = k
    assert actual == expected


def test_k_greater_than_linked_list(multiple_nodes):
    # ?[2] Where k is greater than the length of the linked list
    k = 6
    actual = multiple_nodes.kthFromEnd(k)
    expected = "The value does not exist."

    assert actual == expected


def test_negative_k(multiple_nodes):
    # ?[3] Where k is not a positive integer
    k = -3
    actual = multiple_nodes.kthFromEnd(k)
    expected = "Negative numbres or non-integer numbers not acceptable."

    assert actual == expected


def test_linked_list_size_is_1(one_node):
    # ? [4] Where the linked list is of a size 1
    actual = one_node.get_ll_length()
    expected = 1

    assert actual == expected


def test_at_middle(multiple_nodes):
    # ? [5]“Happy Path” where k is not at the end, but somewhere in the middle of the linked list

    k = 2
    actual = multiple_nodes.kthFromEnd(k)
    expected = "C"

    assert actual == expected


@pytest.fixture
def ll():
    ll = LinkedList()
    return ll


@pytest.fixture
def one_node():
    first_node = LinkedList()
    first_node.insert(Node("A"))
    return first_node


@pytest.fixture
def multiple_nodes():
    nodes = LinkedList()
    nodes.insert(Node("A"))
    nodes.insert(Node("B"))
    nodes.insert(Node("C"))
    nodes.insert(Node("D"))
    return nodes
