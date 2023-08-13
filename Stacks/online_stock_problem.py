# Brute force
def calculateSpan(arr):
    res = []

    for i in range(len(arr)):
        j = i - 1
        while j >= 0:
            if arr[j] > arr[i]:
                # res.append(arr[j]) # if you want to return the nearest greater element to left
                res.append(i - j)
                break

            j -= 1
        else:
            res.append(-1)

    return res


print(calculateSpan([100, 80, 60, 70, 60, 75, 85]))
