def InsertionSort(arr):
  # loop for rounds
  for i in range(1, len(arr)):
    temp = arr[i]
    j = i-1 
    # for j in range(i-1, 0):
    while j >= 0: # and temp < arr[j]
      if arr[j] > temp:
        arr[j+1] = arr[j]
      else:
        break
      
      j -= 1 
      
    arr[j+1] = temp

  return arr



print("Sorted array: ", InsertionSort([2, 12, 1, 9, 3, 6, 34, 8]))