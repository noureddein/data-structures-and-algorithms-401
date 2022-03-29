
arr = [1, 2, 3, 5, 6, 7]
key = 2


def binary_search(arr, key):
    """
        This function search for an element inside the array
        using the binary search method
    """
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = int((l+r) / 2)
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            r = mid - 1
        elif arr[mid] < key:
            l = mid+1
    return -1


print(binary_search(arr, key))
