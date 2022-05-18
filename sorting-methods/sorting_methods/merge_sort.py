class CustomError(Exception):
    pass


class Sorting:
    def _validate_items(self, _list):
        if len(_list) == 0:
            raise CustomError("Empty list not allowed.")
        for item in _list:
            if not isinstance(item, int):
                raise CustomError("Your list has non-integer item.")

    @classmethod
    def merge_sort(cls, arr):
        cls._validate_items(cls, arr)
        n = len(arr)

        if n > 1:
            mid = n // 2
            left = arr[:mid]
            right = arr[mid:]
            cls.merge_sort(left)
            cls.merge_sort(right)
            cls._merge(cls, left, right, arr)

    def _merge(self, left, right, arr):
        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i = i + 1
            else:
                arr[k] = right[j]
                j = j + 1

            k = k + 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


if __name__ == "__main__":
    regular = [8, 4, 23, 42, 16, 15]
    reverse_sorted = [20, 18, 12, 8, 5, -2]
    few_uniques = [5, 12, 7, 5, 5, 7]
    nearly_sorted = [2, 3, 5, 7, 13, 11]
    long_list = [
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
    ]
    Sorting.merge_sort(long_list)
    print(long_list)
