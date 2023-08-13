# Better o(n*2)
# def find_index(arr, k):
#     for i in range(len(arr)):
#         sum = 0
#         for j in range(i, len(arr)):
#             sum += arr[j]

#             if sum == k:
#                 return [i + 1, j + 1]

#     return -1


# Optimal
def find_index(arr, k):
    return -1


print(find_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 21))
