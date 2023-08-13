def binary_search(arr, key):
  left, right = 0, len(arr)-1  # (start, end)
  # mid = (left+right)//2
  mid = left + (right-left)//2  # when integer value is out of bound (2*31-1) (chalaki)

  while left <= right:
    if arr[mid] == key:
      return mid
    # go to right wala part 
    elif key > arr[mid]:
      left = mid + 1
    # go to left wala part 
    else:
      right = mid - 1

    # left and right are updated, so update mid as well
    mid = left  + (right-left)//2

  return -1 


print(binary_search([12, 34, 45, 56, 78], 56))