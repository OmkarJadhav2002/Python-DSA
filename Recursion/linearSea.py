def linearSearch(arr, n, key):

  # iterative approach
  # if len(arr) == 0:
  #     print("Please enter at least one element.")
  # for i in range(0, n-1):
  #   if arr[i] == key:
  #     return i 

  # return -1

  # recursive approach  
  # base case 
  if n == 0:
    return False
  
  # recursive relation 
  if arr[0] == key:
    return True 
  else:
    remainingPortion = linearSearch(arr[1:], n-1, key)
    return remainingPortion


if __name__ == '__main__':
  arr = [1, 4, 6, 12, 2]
  n = len(arr)
  key = 22
  res = linearSearch(arr, n, key)
  if res:
    print("Element found")
  else:
    print("Element not found")
  # if res == -1:
  #   print("Element not found")
  # else:
  #   print("Element found at index: ", res)
