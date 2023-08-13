
def reverse_array(arr):

  start, end = 0, len(arr)-1

  while start < end:
    
    arr[start], arr[end] = arr[end], arr[start]

    start += 1
    end -= 1

  return arr 

# print("Reversed array: ", reverse_array([1, 2, 3, 4, 5]))


print(str(sorted(A)))