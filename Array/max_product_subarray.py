# Find the maximum product subarray


def find_maxProd(arr):
    maxi = float("-inf")

    for i in range(len(arr)):
        prod = 1
        for j in range(i, len(arr)):
            prod *= arr[j]

            maxi = max(prod, maxi)

    return maxi


print(find_maxProd([2, 3, -2, 4]))
