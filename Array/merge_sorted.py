
def merge_array(arr1, n, arr2, m):
  arr3 = [None] * (n+m)
  i, j, k = 0, 0, 0

  while i < n and j < m:
    if arr1[i] < arr2[j]:
      arr3[k] = arr1[i]
      k += 1
      i += 1
    else:
      arr3[k] = arr2[j]
      k += 1
      j += 1

  # add the remaining elements
  while i < n:
    arr3[k] = arr1[i]
    k += 1
    i += 1

  while j < m:
    arr3[k] = arr2[j]
    k += 1
    j += 1

  return arr3


print("Sorted array: ", merge_array([1, 3, 5, 5, 7, 9], 6, [2, 4, 6], 3))  