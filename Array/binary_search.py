# Implementation of Binary-Search

def binarySearch(arr, key):
  start, end = 0, len(arr)-1
  mid = (start+end)//2

  while start<=end:
    if arr[mid] == key:
      return mid
    # go to rigth part of the array 
    elif arr[mid] < key:
      start = mid+1
    # go to left part of the array 
    else:
      end = mid-1

    mid = (start+end)//2

  return -1

if __name__ == '__main__':
  arr = [12, 34, 1, 90, 8, 34]
  elem = int(input("Enter the number you want to search for: "))
  ans = binarySearch(arr, elem)
  if ans or ans==0:
    print("Element found.")
  else:
    print("Element not found.")

# def binary_search(arr, key):
#   left, right = 0, len(arr)-1  # (start, end)
#   # mid = (left+right)//2
#   mid = left + (right-left)//2  # when integer value is out of bound (2*31-1) (chalaki)

#   while left <= right:
#     if arr[mid] == key:
#       return mid
#     # go to right wala part 
#     elif key > arr[mid]:
#       left = mid + 1
#     # go to left wala part 
#     else:
#       right = mid - 1

#     # left and right are updated, so update mid as well
#     mid = left  + (right-left)//2

#   return -1 

# if __name__ == '__main__':
#   arr = [12, 34, 45, 56, 78]
#   ans = binary_search(arr, 78)
#   if ans or ans==0:
#     print("Element found")
#   else:
#     print("Not found")

# l = [12, 3, 4, 5, 6, 7]
# print(l.pop(2))

