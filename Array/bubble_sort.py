
# outer loop for rounds 
def BubbleSort(arr):
  for i in range(1, len(arr)):
    swapped = False
    for j in range(0, len(arr)-i):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        swapped = True

    if swapped == False:
      break
  
  return arr

print("Sorted array: ", BubbleSort([10, 1, 7, 6, 14, 9]))
