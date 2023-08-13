# find the row with maximum number of ones


def find_row(arr, n, m):
    # brute force (calculate the number of 1's in each row)
    res = []
    for i in range(n):
        count = 0
        for j in range(m):
            if arr[i][j] == 1:
                count += 1
        res.append(count)

    mini = float("inf")
    mini_row = -1
    for i in range(len(res)):
        if res[i] < mini:
            mini = res[i]
            mini_row = i

    return mini_row
    # maxi = float("-inf")
    # for i in range(len(res)):
    #     if res[i] > maxi:
    #         maxi = i
    #         break
    # return maxi


print(find_row([[1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 1, 1, 1]], 4, 4))
