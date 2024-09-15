# problem type: Sliding window problem
# code to find max sum of a subarray of size k
# More optimized approach than slidingwindow01.py


def get_max_sum_of_subarr(arr, window_size):
    
    # edge case 
    if window_size > len(arr):
        return None
    
    max_sum = sum(arr[:window_size])
    window_ele_sum = max_sum
    max_sum_subarr_start_idx = 0

    for end_idx in range(window_size, len(arr)):
        window_ele_sum += arr[end_idx] - arr[end_idx - window_size]

        if window_ele_sum > max_sum:
            max_sum = window_ele_sum
            max_sum_subarr_start_idx = end_idx - window_size + 1
    
    return (max_sum, max_sum_subarr_start_idx, max_sum_subarr_start_idx + window_size - 1)


arr = [1,2,3,4]
window_size = 2

mx, st_idx, ed_idx =  get_max_sum_of_subarr(arr, window_size)

print(f'Max sum of any subarray of size {window_size} is : {mx}, start idx: {st_idx}, end idx: {ed_idx}')

print(f"Subarray is : {arr[st_idx: ed_idx+1]}")