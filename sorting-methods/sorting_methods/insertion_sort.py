class CustomError(Exception):
    pass


def validate_items(_list):
    if len(_list) == 0:
        raise CustomError("Empty list not allowed.")
    for item in _list:
        if not isinstance(item, int):
            raise CustomError("Your list has non-integer item.")


def insertion_sort(arr):
    validate_items(arr)
    n = len(arr)
    for i, val1 in enumerate(arr):  # for (i=0, condition, i++) for i in len(arr)
        # arr[i]
        min = i
        j = i
        for _ in arr:
            j += 1
            if j > n - 1:
                break
            if arr[j] < arr[min]:
                min = j
        temp = arr[min]
        arr[min] = arr[i]
        arr[i] = temp
    return arr


if __name__ == "__main__":
    print(insertion_sort([2, 3, 5, 7, 13, 1]))
    # print(selection_sort([]))
