def nearest_greater(s):
    res = []
    for i in range(len(s)):
        ng = -1
        for j in range(i + 1, len(s)):
            if s[j] > s[i]:
                ng = s[j]
                break

        res.append(ng)

    return res


print(nearest_greater([1, 2, 5, 1, 12]))
