# Brute Force
# def nearest_greater_left(arr):
#     res = []

#     for i in range(len(arr)):
#         j = i - 1
#         while j >= 0:
#             if arr[j] > arr[i]:
#                 res.append(arr[j])
#                 break
#             j -= 1

#         else:
#             res.append(-1)

#     return res


# Optimal (Using stack)
def nearest_greater_left(arr):
    res = []
    stack = []

    for i in range(len(arr)):
        if len(stack) == 0:
            res.append(-1)

        elif len(stack) > 0 and stack[-1] > arr[i]:
            res.append(stack[-1])

        elif len(stack) > 0 and stack[-1] < arr[i]:
            while len(stack) > 0 and arr[stack[-1]] < arr[i]:
                stack.pop()

            if len(stack) == 0:
                res.append(-1)
            else:
                res.append(stack[-1])

        stack.append(i)

    return res


print(nearest_greater_left([100, 80, 60, 70, 60, 75, 85]))
