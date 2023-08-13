# Reverse an array
# def reverse_array(arr):
#   l, r = 0, len(arr)-1

#   while l <= r:
#     arr[l], arr[r] = arr[r], arr[l]

#     l += 1
#     r -= 1

#   return arr

# print("Reversed array: ", reverse_array([1, 2, 3, 4, 5, 6]))

# Merge two sorted array 
def merge_sortedArrays(arr1, arr2, arr3):
  i, j = 0, 0 # one pointer to first array and another pointer for second array
  k = 0 # third array to store the result

  while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
      arr3[k] = arr1[i]
      k += 1
      i += 1
    else:
      arr3[k] = arr2[j]
      k += 1
      j += 1

  # copy the remaining elements of arr1 
  while i < len(arr1):
    arr3[k] = arr1[i]
    k += 1
    i += 1

  # copy the remaining elements of arr2
  while j < len(arr2):
    arr3[k] = arr2[j]
    k += 1
    j += 1

  return arr3

if __name__ == '__main__':
  arr1 = [1, 3, 5, 7, 9]
  arr2 = [2, 4, 6]
  arr3 = [0] * (len(arr1) + len(arr2)) 

  res = merge_sortedArrays(arr1, arr2, arr3)
  print("Sorted array after merging two arrays: ", res)