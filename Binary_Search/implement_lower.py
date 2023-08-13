# Implement lower bound
def implement_lower_bound(arr, x):
    # optimal (Binary search)
    l, r = 0, len(arr) - 1
    res = len(arr)
    while l <= r:
        mid = (l + r) // 2

        if arr[mid] >= x:
            res = mid
            r = mid - 1
        else:
            l = mid + 1

    return res

    # Brute force
    # n = len(arr)
    # for i in range(len(arr)):
    #     if arr[i] >= x:
    #         return i

    # return n


print(implement_lower_bound([1, 2, 2, 3, 3, 5], 2))
