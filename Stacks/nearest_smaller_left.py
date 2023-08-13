# Brute force
# def nearest_smaller_left(arr):
#     res = []
#     for i in range(len(arr)):
#         ns = -1
#         for j in range(i - 1, -1, -1):
#             if arr[j] < arr[i]:
#                 ns = arr[j]
#                 break

#         res.append(ns)

#     return res


# print(nearest_smaller_left([1, 6, 2]))
# Optimal (using stack)
def find_nearest_smaller_left(arr):
    stack = []
    res = []

    for i in range(len(arr)):
        if len(stack) == 0:
            res.append(-1)

        elif len(stack) > 0 and stack[-1] <= arr[i]:
            res.append(stack[-1])

        else:
            if len(stack) > 0 and stack[-1] > arr[i]:
                while len(stack) > 0 and stack[-1] <= arr[i]:
                    stack.pop()

                if len(stack) == 0:
                    res.append(-1)

                else:
                    res.append(stack[-1])

        stack.append(arr[i])

        return res


# if __name__ == "__main__":
#     arr = [1, 6, 2]
#     ans = find_nearest_smaller_left(arr)
#     print("Output: ", ans)
