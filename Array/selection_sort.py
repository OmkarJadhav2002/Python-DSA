def selection_sort(arr):
  
  for i in range(len(arr)-1):
    minIndex = i
    for j in range(i+1, len(arr)):
      if arr[j] < arr[minIndex]:
        minIndex = j

    arr[minIndex], arr[i] = arr[i], arr[minIndex]

  return arr

print("Sorted array: ", selection_sort([12, 3, 1, 7, 9]))