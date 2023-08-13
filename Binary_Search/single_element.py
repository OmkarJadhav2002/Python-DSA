# Find single element in sorted array
def find_element(arr):
    # Optimal (Binary Search)
    pass

    # # Brute force
    # if len(arr) == 1:
    #   return arr[0]

    # for i in range(len(arr)):
    #   # if first element
    #   if i == 0:
    #     if arr[i] != arr[i+1]:
    #       return arr[i]

    #   # if second element
    #   if i == len(arr)-1:
    #     if arr[i] != arr[i-1]:
    #       return arr[i]

    #   # for remaining elements
    #   else:
    #     if arr[i] != arr[i-1] and arr[i] != arr[i+1]:
    #       return arr[i]

    # # if not found return -1
    # return -1


if __name__ == "__main__":
    res = find_element([1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5])

    if res != -1:
        print("Single element: ", res)
    else:
        print("Element not found.")
