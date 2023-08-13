# Find maximum array sum


# def find_max_sum(arr):
#     maxsum = arr[0]
#     currentsum = 0

#     for i in range(len(arr)):
#         currentsum += arr[i]
#         if currentsum > maxsum:
#             maxsum = currentsum
#         if currentsum < 0:
#             currentsum = 0

#     return maxsum


# Find the subarray with maximum sum
def find_max_sum(arr):
    maxsum = float("-inf")
    currentsum = 0
    start = 0
    res_start = 0
    res_end = 0
    for i in range(len(arr)):
        currentsum += arr[i]

        if currentsum > maxsum:
            maxsum = currentsum
            res_start, res_end = start, i
        if currentsum < 0:
            currentsum = 0
            start = i + 1  # ***

    return maxsum, arr[res_start : res_end + 1]


print(find_max_sum([-2, -3, 4, -1, -2, 1, 5, -3]))
