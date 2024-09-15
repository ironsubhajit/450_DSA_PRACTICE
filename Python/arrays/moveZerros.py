def move_zeros_to_left(arr):
    i = 0
    for j in range(len(arr)):
        if arr[j] == 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    return arr


def move_zeros_to_right(arr):
    pass


arr = [0, 1, 0, 0, 2, 0, 3]
print("Original array: ", arr)
move_zeros_to_left(arr)
print("Zero shifted array: ", arr)
