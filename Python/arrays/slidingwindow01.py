arr = [2, 3, 1, 1, 4, 3, 6, 7, 2]
size_arr = 9
window_size = 3



def get_max_subarr_sum(window_size):
    start_idx = 0
    end_idx = 0

    window_ele_sum = 0
    max_sum = 0
    max_sum_subarr_start_idx = 0
    max_sum_subarr_end_idx = 0

    while(end_idx < len(arr)):
        window_ele_sum += arr[end_idx]

        if (end_idx - start_idx + 1 < window_size):
            end_idx += 1
        elif (end_idx - start_idx + 1 == window_size):
            if window_ele_sum > max_sum:
                max_sum = window_ele_sum
                max_sum_subarr_start_idx = start_idx
                max_sum_subarr_end_idx = end_idx
            
            window_ele_sum = window_ele_sum - arr[start_idx]
            start_idx += 1
            end_idx += 1

    return (max_sum, max_sum_subarr_start_idx, max_sum_subarr_end_idx)


mx, st_idx, ed_idx =  get_max_subarr_sum(window_size)

print(f'Max sum of any subarray of size {window_size} is : {mx}, start idx: {st_idx}, end idx: {ed_idx}')

print("Subarray is : ", end="")
for i in range(st_idx, ed_idx+1):
    print(arr[i], end=" ")