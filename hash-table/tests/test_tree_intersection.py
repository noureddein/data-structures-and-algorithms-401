from binarytree import build2
import pytest

from hash_table.hash_map import HashTable
from hash_table.tree_intersection import TreeIntersection


@pytest.mark.parametrize("capacity", [10, 5, 30, 100, 1024])
def test_expected_outcome_with_tree_numbers(create_trees, capacity):
    tree_1, tree_2 = create_trees
    ht = TreeIntersection(capacity)

    actual = ht.tree_intersection(tree_1, tree_2)
    expected = [100, 160, 200, 350, 125, 175, 500]
    assert actual == expected


@pytest.mark.parametrize("capacity", [5, 10, 30, 100, 1024])
def test_expected_outcome_with_tree_characters(create_char_trees, capacity):
    tree_1, tree_2 = create_char_trees
    ht_char = TreeIntersection(capacity)

    actual = ht_char.tree_intersection(tree_1, tree_2)
    expected = ["A", "C"]
    assert actual == expected


def test_expected_failure():
    ht = TreeIntersection()
    with pytest.raises(Exception):
        ht.tree_intersection("", "")


@pytest.fixture
def create_char_trees():
    tree_1_values = ["A", "B", "C", "D"]
    tree_2_values = ["A", "F", "C", "H"]

    tree_1 = build2(tree_1_values)
    tree_2 = build2(tree_2_values)
    return tree_1, tree_2


@pytest.fixture
def create_trees():
    tree_1_values = [42, 100, 600, 15, 160, 200, 350, 125, 175, 4, 500]
    tree_2_values = [150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500]

    tree_1 = build2(tree_1_values)
    tree_2 = build2(tree_2_values)
    return tree_1, tree_2
