# Implementation of Binary Search (Iterative)

def binary_search(arr, num):
  start, end = 0, len(arr)-1

  while start <= end:
    mid = (start+end)//2

    if arr[mid] == num:
      return mid 
    elif num > arr[mid]:
      start = mid + 1
    else:
      end = mid - 1

  return -1

print(binary_search([1, 2, 34, 12, 0, 23, 45], 45))

# Questions 
# Implement Upper bound 
# Implement Lower bound 
# Floor and Ceil in sorted array 
# Find first and last occurence of an element 
