# problem type: sliding window
# Print first -ve integer in every window of size k


def print_first_neg_num_of_window(arr, window_size):

    arr_size = len(arr)

    # Edge case
    if window_size > arr_size:
        return None

    start_idx = 0
    end_idx = 0

    neg_num_list = []

    while end_idx < arr_size:

        if arr[end_idx] < 0:
            neg_num_list.append(arr[end_idx])

        if (end_idx - start_idx + 1 < window_size):
            end_idx += 1
        elif (end_idx - start_idx + 1 == window_size):
            if len(neg_num_list) == 0:
                print(0, end=" ")
            else:
                print(neg_num_list[0], end=' ')
                if neg_num_list[0] == arr[start_idx]:
                    neg_num_list.pop(0)
            end_idx += 1
            start_idx += 1


from collections import deque

def print_first_neg_num_of_window_2(arr, window_size):
    # More optimized approach as it uses less code and deque
    arr_size = len(arr)

    # edge case
    if window_size > arr_size:
        return None

    # using deque to store indices of neg numbers in the current array
    neg_num_indices = deque()

    for end_idx in range(arr_size):
        if arr[end_idx] < 0:
            neg_num_indices.append(end_idx)

        # check window is valid
        if end_idx >= window_size - 1:
            if neg_num_indices:
                print(arr[neg_num_indices[0]], end=" ")
            else:
                # if there is no negative number then print 0
                print(0, end=" ")

            # remove the element that is going out of the window from deque
            if neg_num_indices and neg_num_indices[0] == end_idx - window_size + 1:
                # end_idx - window_size - 1 gives start index of the window
                neg_num_indices.popleft()


input_array = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3

if __name__ == '__main__':
    print_first_neg_num_of_window_2(input_array, k)

