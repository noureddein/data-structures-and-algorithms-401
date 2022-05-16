from selection_insertion.selection_insertion import selection_sort
import pytest

"""
    test cases 
        Random         : [8,4,23,42,16,15]
        Reverse-sorted: [20,18,12,8,5,-2]
        Few uniques: [5,12,7,5,5,7]
        Nearly-sorted: [2,3,5,7,13,11]


"""


def test_random_list():
    actual = selection_sort([8, 4, 23, 42, 16, 15])
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


def test_reverse_sorted():
    actual = selection_sort([20, 18, 12, 8, 5, -2])
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected


def test_few_uniques():
    actual = selection_sort([5, 12, 7, 5, 5, 7])
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected


def test_nearly_sorted():
    actual = selection_sort([2, 3, 5, 7, 13, 11])
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected


def test_non_integer_elements():
    with pytest.raises(Exception):
        selection_sort([1, 4, "3"])


def test_pass_empty_list():
    with pytest.raises(Exception):
        selection_sort([])
