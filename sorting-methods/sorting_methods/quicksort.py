class CustomError(Exception):
    pass


class QuickSort:
    @classmethod
    def quick_sort(cls, arr):
        if not isinstance(arr, list):
            raise CustomError("Your input is not a type of list/array.")
        left = 0
        right = len(arr) - 1
        cls.helper_quick_sort(cls, arr, left, right)

    def helper_quick_sort(self, arr, left, right):
        if left < right:
            position = self._partition(self, arr, left, right)
            self.helper_quick_sort(self, arr, left, position - 1)
            self.helper_quick_sort(self, arr, position + 1, right)

    def _partition(self, arr, left, right):
        pivot = arr[right]
        i = left - 1
        for j in range(left, right):
            if arr[j] <= pivot:
                i += 1
                self._swap(self, arr, i, j)

        self._swap(self, arr, i + 1, right)
        return i + 1

    def _swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp


if __name__ == "__main__":
    arr = [
        [8, 4, 23, 42, 16, 15],
        [20, 18, 12, 8, 5, -2],
        [5, 12, 7, 5, 5, 7],
        [2, 3, 5, 7, 13, 11],
    ]
    for item in arr:
        QuickSort.quick_sort(item)
        print(item)
