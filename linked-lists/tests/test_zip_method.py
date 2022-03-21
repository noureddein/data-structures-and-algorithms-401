import pytest
from linked_lists.linked_list import LinkedList
from linked_lists.node import Node


def test_equally_lists(ll_1, ll_2):
    # ll = LinkedList()
    zipped_list = LinkedList.zip_list(ll_1, ll_2)

    actual = zipped_list.to_string()
    expected = (
        "{ A } -> { 1 } -> { B } -> { 2 } -> { C } -> { 3 } -> { D } -> { 4 } -> Null"
    )

    assert actual == expected

    actual = zipped_list.kthFromEnd(6)
    expected = 1

    assert actual == expected


def test_first_list_greater_than_second_list(ll_1, ll_two_item):
    ll = LinkedList()
    zipped_list = ll.zip_list(ll_1, ll_two_item)

    actual = zipped_list.to_string()
    expected = "{ A } -> { 1 } -> { B } -> { 2 } -> { C } -> { D } -> Null"

    assert actual == expected

    actual = zipped_list.kthFromEnd(2)
    expected = 2

    assert actual == expected


def test_first_list_less_than_second_list(ll_two_item, ll_1):
    ll = LinkedList()
    zipped_list = ll.zip_list(ll_two_item, ll_1)

    actual = zipped_list.to_string()
    expected = "{ 1 } -> { A } -> { 2 } -> { B } -> { C } -> { D } -> Null"

    assert actual == expected

    actual = zipped_list.kthFromEnd(5)
    expected = 1

    assert actual == expected


@pytest.fixture
def ll_1():
    nodes = LinkedList()
    nodes.insert(Node("D"))
    nodes.insert(Node("C"))
    nodes.insert(Node("B"))
    nodes.insert(Node("A"))
    return nodes


@pytest.fixture
def ll_2():
    nodes = LinkedList()
    nodes.insert(Node(4))
    nodes.insert(Node(3))
    nodes.insert(Node(2))
    nodes.insert(Node(1))
    return nodes


@pytest.fixture
def ll_two_item():
    nodes = LinkedList()
    nodes.insert(Node(2))
    nodes.insert(Node(1))
    return nodes
