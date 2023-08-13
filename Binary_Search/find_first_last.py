# find the first and last occurence of the element


def find_first_last_occurence(arr, num):
    # Brute force
    first, last = -1, -1

    for i in range(len(arr)):
        if arr[i] == num:
            if first == -1:
                first = i

            last = i

    return [first, last]


print(find_first_last_occurence([5, 7, 7, 8, 8, 10], 6))
