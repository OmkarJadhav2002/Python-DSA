# Brute force
# def nearest_smaller_right(arr):
#     res = []

#     for i in range(len(arr)):
#         nearest_smaller = -1
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[i]:
#                 nearest_smaller = arr[j]
#                 break

#         res.append(nearest_smaller)

#     return res


# print(nearest_smaller_right([3, 8, 5, 2, 25]))


# Optimal (Using Stack)
def nearest_smaller_right(arr):
    res = []
    stack = []

    for i in range(len(arr) - 1, -1, -1):
        if len(stack) == 0:
            res.append(-1)

        elif len(stack) > 0 and stack[-1] <= arr[i]:
            res.append(stack[-1])

        elif len(stack) > 0 and stack[-1] > arr[i]:
            while len(stack) > 0 and stack[-1] > arr[i]:
                stack.pop()

            if len(stack) == 0:
                res.append(-1)
            else:
                res.append(stack[-1])

        stack.append(arr[i])

    return res[::-1]
