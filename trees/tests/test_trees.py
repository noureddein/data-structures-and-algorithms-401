from trees.binary_tree import TreeNode, BinaryTree, BinarySearchTree
import pytest

"""
    Note:
        For the question --> Can successfully instantiate an empty tree
        it can not be instantiated empty, because the tree should have a root
"""


def test_pre_order(multi_nodes):
    # Can successfully return a collection from a preorder traversal
    root = multi_nodes
    binary_tree = BinaryTree(root)
    actual = binary_tree.pre_order()
    expected = ["A", "B", "D", "E", "C", "F"]

    assert expected == actual


def test_in_order(multi_nodes):
    # Can successfully return a collection from an inorder traversal
    root = multi_nodes
    binary_tree = BinaryTree(root)
    actual = binary_tree.in_order()
    expected = ["D", "B", "E", "A", "F", "C"]

    assert expected == actual


def test_post_order(multi_nodes):
    # Can successfully return a collection from a postorder traversal
    root = multi_nodes
    binary_tree = BinaryTree(root)
    actual = binary_tree.post_order()
    expected = ["D", "E", "B", "F", "C", "A"]

    assert expected == actual


def test_exception(test_node):
    root = test_node

    with pytest.raises(Exception):
        tree = BinaryTree(root)


def test_single_root():
    # Can successfully instantiate a tree with a single root node
    tree = BinarySearchTree(TreeNode(1))
    actual = tree.breadth_first()
    expected = [1]

    assert actual == expected


def test_add_left_right_child(tree_with_empty_third_level):
    # For a Binary Search Tree, can successfully add a left child and right child properly to a node
    bst = BinarySearchTree(tree_with_empty_third_level)
    actual = bst.breadth_first()
    expected = ["A", "B", "C"]

    assert actual == expected

    # Add a left child for B node
    actual = bst.add(1)
    expected = ["A", "B"]

    assert actual == expected

    # Add a right child for B node
    actual = bst.add(2)
    expected = ["A", "B"]

    assert actual == expected


def test_contains(tree_with_empty_third_level):
    # Test contains method
    root = tree_with_empty_third_level
    bst = BinarySearchTree(root)
    actual = bst.contains("A")
    expected = True

    assert actual == expected

    actual = bst.contains("F")
    expected = False

    assert actual == expected


@pytest.fixture
def multi_nodes():
    a = TreeNode("A")
    b = TreeNode("B")
    c = TreeNode("C")
    d = TreeNode("D")
    e = TreeNode("E")
    f = TreeNode("F")

    a.left = b
    a.right = c

    b.left = d
    b.right = e

    c.left = f

    return a


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
