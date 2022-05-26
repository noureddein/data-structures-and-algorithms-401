import pytest
from sorting_methods.quicksort import QuickSort

"""
Reverse-sorted: [20,18,12,8,5,-2]
Few uniques: [5,12,7,5,5,7]
Nearly-sorted: [2,3,5,7,13,11]
"""


@pytest.mark.parametrize(
    "unsorted, sorted",
    [
        ([8, 4, 23, 42, 16, 15], [4, 8, 15, 16, 23, 42]),
        ([20, 18, 12, 8, 5, -2], [-2, 5, 8, 12, 18, 20]),
        ([5, 12, 7, 5, 5, 7], [5, 5, 5, 7, 7, 12]),
        ([2, 3, 5, 7, 13, 11], [2, 3, 5, 7, 11, 13]),
        (["c", "a", "h", "d"], ["a", "c", "d", "h"]),
    ],
)
def test_cases(unsorted, sorted):
    QuickSort.quick_sort(unsorted)
    assert unsorted == sorted


def test_failure():
    with pytest.raises(Exception):
        QuickSort.quick_sort("a")
