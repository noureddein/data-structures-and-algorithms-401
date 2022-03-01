def insertShiftArray(arr, val):
    if type(arr) != list:
        return "Should receive an array"

    if len(arr) == 0:
        return arr + [val]

    if len(arr) % 2 == 0:
        index = len(arr) / 2

    if len(arr) % 2 == 1:
        index = len(arr)/2 + 1

    index = int(index)
    arr = arr[0:index] + [val] + arr[index:]

    return arr


print(insertShiftArray([1, 2, 4, 3], 7))
