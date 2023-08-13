# Implement upper bound
def implement_upper_bound(arr, x):
    # optimal (Binary search)
    l, r = 0, len(arr) - 1
    res = len(arr)
    while l <= r:
        mid = (l + r) // 2

        if arr[mid] > x:
            res = mid
            r = mid - 1
        else:
            l = mid + 1

    return res

    # Brute force (linear search O(n))
    # n = len(arr)
    # for i in range(len(arr)):
    #     if arr[i] > x:
    #         return i

    # return n


print(implement_upper_bound([2, 4, 6, 7], 4))
