def selection_sort_recursive(arr, i=0):
    if i < len(arr) - 1:
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

        selection_sort_recursive(arr, i + 1)


# Example usage:
arr = [64, 25, 12, 22, 11]
selection_sort_recursive(arr)
print("Sorted array:", arr)
