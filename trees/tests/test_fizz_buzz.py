import pytest
from trees.binary_tree import TreeNode
from trees.fizz_buzz import FizzBuzz
from trees.k_ary import KTreeNode


def test_tree_node_type(binary_tree_node):
    # Test different type of tree node object
    with pytest.raises(Exception):
        FizzBuzz(binary_tree_node)


def test_fizz_buzz_logic(k_tree_of_numbers):
    # Test the fizz buzz logic function
    fizz_buzz = FizzBuzz(k_tree_of_numbers)
    actual = fizz_buzz._fizz_buzz_logic(3)
    expected = 'Fizz'
    assert actual == expected


def test_fizz_buzz_tree(k_tree_of_numbers):
    # Test fizz buzz tree function and return the expected values
    fizz_buzz = FizzBuzz(k_tree_of_numbers)
    new_tree = fizz_buzz.fizz_buzz_tree()
    actual = new_tree.value
    expected = 'FizzBuzz'
    assert actual == expected


def test_fizz_buzz_with_mixed_values(k_tree_of_mixed_values):
    # Test fizz buzz tree function with a mixed values of numbers and characters
    fizz_buzz = FizzBuzz(k_tree_of_mixed_values)
    with pytest.raises(Exception):
        new_tree = fizz_buzz.fizz_buzz_tree()


@pytest.fixture
def k_tree_of_numbers():
    childrenNodes = [
        KTreeNode(1, [KTreeNode(4), KTreeNode(5)]),
        KTreeNode(2, [KTreeNode(6)]),
        KTreeNode(3, [KTreeNode(7)])
    ]
    k_ary = KTreeNode(0, childrenNodes)
    return k_ary


@pytest.fixture
def k_tree_of_mixed_values():
    childrenNodes = [
        KTreeNode(1, [KTreeNode(4), KTreeNode('A')]),
    ]
    k_ary = KTreeNode(3, childrenNodes)
    return k_ary


@pytest.fixture
def binary_tree_node():
    binary_tree = TreeNode('A')
    binary_tree.left = TreeNode('B')
    binary_tree.right = TreeNode('C')
    return binary_tree
