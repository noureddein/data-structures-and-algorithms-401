from sorting_methods.merge_sort import Sorting
import pytest


def test_random_list():
    tested_array = [8, 4, 23, 42, 16, 15]
    Sorting.merge_sort(tested_array)
    actual = tested_array
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


def test_reverse_sorted():
    tested_array = [20, 18, 12, 8, 5, -2]
    Sorting.merge_sort(tested_array)
    actual = tested_array
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected


def test_few_uniques():
    tested_array = [5, 12, 7, 5, 5, 7]
    Sorting.merge_sort(tested_array)
    actual = tested_array
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected


def test_nearly_sorted():
    tested_array = [2, 3, 5, 7, 13, 11]
    Sorting.merge_sort(tested_array)
    actual = tested_array
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected


def test_long_array_sorted():
    tested_array = [
        8,
        4,
        23,
        42,
        16,
        15,
        20,
        18,
        12,
        8,
        5,
        -2,
        5,
        12,
        7,
        5,
        5,
        7,
        2,
        3,
        5,
        7,
        13,
        11,
        40,
        12,
        33,
        6,
        90,
        33,
        14,
        13,
        43,
    ]
    Sorting.merge_sort(tested_array)
    actual = tested_array
    expected = [
        -2,
        2,
        3,
        4,
        5,
        5,
        5,
        5,
        5,
        6,
        7,
        7,
        7,
        8,
        8,
        11,
        12,
        12,
        12,
        13,
        13,
        14,
        15,
        16,
        18,
        20,
        23,
        33,
        33,
        40,
        42,
        43,
        90,
    ]
    assert actual == expected


def test_non_integer_elements():
    with pytest.raises(Exception):
        Sorting.merge_sort([1, 4, "3"])


def test_pass_empty_list():
    with pytest.raises(Exception):
        Sorting.merge_sort([])
