# Find the minimum in Rotated Sorted Array 

def find_minimum(arr):
  mini = arr[0]
  i = 0
  j = 1

  while i<=j and j < len(arr):
    if arr[i]<mini:
      mini = arr[i]
    if arr[j]<mini:
      mini = arr[j]

    i += 1
    j +=1

  return mini

print("Minimum element in an array: ", find_minimum([4, 5, 0, 1, 12, 7, 90]))