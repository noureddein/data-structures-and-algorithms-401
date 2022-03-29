def reverse_array(item):
    if type(item) != list:
        return 'Should receive an array'

    new_array = []
    arr_len = len(item)

    if not arr_len:
        return 'Empty list'
    if arr_len == 1:
        return 'No need to reverse'

    for i in range(arr_len - 1, -1, -1):
        new_array.append(item[i])
    return new_array


x = [
    199, 197, 193, 191, 181, 179, 173, 167, 163, 157, 151, 149, 139, 137, 131, 127, 113, 109, 107, 103,
    101, 97, 89, 83, 79, 73, 71, 67, 61, 59, 53, 47, 43, 41, 37, 31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2
]

print(reverse_array(x))
