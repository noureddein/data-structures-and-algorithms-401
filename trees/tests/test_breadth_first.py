from trees.breadth_first import breadth_first
from trees.binary_tree import TreeNode, BinarySearchTree
from trees.custom_error import CustomError
import pytest


def test_three_values(tree_with_empty_third_level):
    root = tree_with_empty_third_level
    actual = breadth_first(root)
    expected = ['A', 'B', 'C']

    assert actual == expected


def test_tree_of_numbers(tree_of_numbers):
    root = tree_of_numbers
    actual = breadth_first(root)
    expected = [2, 7, 5, 2, 6, 9, 5, 11, 4]

    assert actual == expected


def test_failure_diff_type_of_node(test_node):
    root = test_node
    with pytest.raises(CustomError):
        breadth_first(root)


@pytest.fixture
def test_node():
    class Node:
        def __init__(self, val) -> None:
            self.val = val
            self.next = None

    node = Node("Test")
    return node


@pytest.fixture
def tree_with_empty_third_level():
    a = TreeNode("A")
    b = TreeNode("B")
    c = TreeNode("C")

    a.left = b
    a.right = c

    return a


@pytest.fixture
def tree_of_numbers():
    root = TreeNode(2)
    bst = BinarySearchTree(root)
    numbers = [7, 5, 2, 6, 9, 5, 11, 4]
    for i in numbers:
        bst.add(i)
    return root
