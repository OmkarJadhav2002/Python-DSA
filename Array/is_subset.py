arr1 = [11, 7, 1, 13, 21, 3, 7, 3]
arr2 = [11, 3, 7, 1, 7]


def isSubset(arr1, arr2):
    res = set()
    for i in arr1:
        res.add(i)

    for i in arr2:
        if i in res:
            continue
        else:
            return False

    return True


print(isSubset([1, 2, 3, 4, 4, 5, 6], [1, 2, 4]))
