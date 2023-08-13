def binary_search_recursive(arr, s, e, key):
  # 1st base case  
  # element not found 
  if s>e:
    return False
   
  # calculate mid
  mid = (s+e)//2

  # 2nd base case  
  if arr[mid] == key:
    return True 

  # recursive relation
  if arr[mid] < key:
    # go to right wala part 
    return binary_search_recursive(arr, mid+1, e, key)
  else:
    # go to left wala part 
    return binary_search_recursive(arr, s, mid-1, key)

if __name__ == '__main__':
  arr = [2, 4, 6, 10, 14, 16]
  res = binary_search_recursive(arr, 0, len(arr)-1, 22)

  if res:
    print("Element found")
  else:
    print("Element not found")