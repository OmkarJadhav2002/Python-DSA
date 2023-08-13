def nearest_smaller_left(arr):
    res = []  # to store the index of nearest smaller element
    stack = []  # for comaparison

    for i in range(len(arr)):
        if len(stack) == 0:
            res.append(-1)

        elif len(stack) > 0 and arr[stack[-1]] <= arr[i]:
            res.append(stack[-1])

        elif len(stack) > 0 and arr[stack[-1]] > arr[i]:
            while len(stack) > 0 and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if len(stack) == 0:
                res.append(-1)
            else:
                res.append(stack[-1])

        stack.append(i)

    return res


def nearest_smaller_right(arr):
    res = []
    stack = []

    pseudoIndex = len(arr)

    for i in range(len(arr) - 1, -1, -1):
        if len(stack) == 0:
            # res.append(-1)
            res.append(pseudoIndex)

        elif len(stack) > 0 and arr[stack[-1]] <= arr[i]:
            res.append(stack[-1])

        elif len(stack) > 0 and arr[stack[-1]] > arr[i]:
            while len(stack) > 0 and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if len(stack) == 0:
                res.append(pseudoIndex)
            else:
                res.append(stack[-1])

        stack.append(i)

    return res[::-1]


def find_max_area(arr):
    left_index = nearest_smaller_left(arr)
    right_index = nearest_smaller_right(arr)

    result = [x - y - 1 for x, y in zip(right_index, left_index)]

    max_area = float("-inf")
    for i in range(len(arr)):
        width = right_index[i] - left_index[i] - 1
        area = arr[i] * width
        max_area = max(max_area, area)

    print(max_area)


find_max_area([9, 10, 4, 10, 4, 5, 16])
