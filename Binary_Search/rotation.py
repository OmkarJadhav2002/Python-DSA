
# Find how many times the sorted array is rotated 

# array contains unique elements 
def find_rotation_unique(arr):
  low, high = 0, len(arr)-1
  mini = float("inf")
  index = -1
  while low<=high:
    mid = (low+high)//2

    if arr[low] <= arr[high]:
      mini = min(mini, arr[low]) 
      index = low
      break 
    
    # if left portion of arr is sorted 
    if arr[low] <= arr[mid]:
      mini = min(mini, arr[low])
      index = low 
      low = mid+1

    # if right portion of arr is sorted 
    else:
      mini = min(mini, arr[mid])
      high = mid-1
      index = mid 

  return index 

# if array contains duplicate elements 
# def find_rotation_duplicate(arr):
#   low, high = 0, len(arr)-1
#   mini = float("inf")
#   index = -1 # to store the index of minimum element (which is answer)

#   while low <= high:
#     mid = (low+high)//2

    # if array already sorted 



# print("Number of rotation: ", find_rotation_unique([3, 4, 5, 1, 2]))

