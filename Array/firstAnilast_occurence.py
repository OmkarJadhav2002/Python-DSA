
# find left-most occurence 
# def find_first_occurence(arr, key):
#   start, end = 0, len(arr)-1
#   mid = (start+end)//2
#   res = -1

#   while start <= end:
#     if arr[mid] == key:
#       # store the value 
#       res = mid
#       end = mid - 1
#     elif key < arr[mid]:
#       end = mid - 1
#     elif key > arr[mid]:
#       start = mid + 1

#     mid = (start+end)//2

#   return res

# find right-most occurence 
# def find_last_occurence(arr, key):
#   start, end = 0, len(arr)-1
#   mid = (start+end)//2
#   res = -1

#   while start <= end:
#     if arr[mid] == key:
#       # store the value 
#       res = mid
#       start = mid + 1
#     elif key < arr[mid]:
#       end = mid -1
#     elif key > arr[mid]:
#       start = mid + 1

#     mid = (start+end)//2

#   return res

# if __name__ == '__main__':
#   arr = [0, 2, 2, 2, 3, 3, 3, 5, 5, 5]
#   first = find_first_occurence(arr, 2)
#   last = find_last_occurence(arr, 2)

#   print("First occurence is at position {} and last occurence is at position {}.".format(first, last))

# using recursion

# def find_left_occurence(arr, start, end, key):
#   if start <= end:
#     mid = (start+end)//2
#     if mid == 0 or key>arr[mid-1] and arr[mid] == key:
#       return mid 
    
#     # recursive call 
#     elif arr[mid] < key:
#       return find_left_occurence(arr, mid+1, end, key)
#     else:
#       return find_left_occurence(arr, start, mid-1, key)

#   return -1

# def find_right_occurence(arr, start, end, key):
#   if start <= end:
#     mid = (start+end)//2
#     if mid == len(arr)-1 or key<arr[mid+1] and arr[mid] == key:
#       return mid 
      
#     # recursive call 
#     elif arr[mid] > key:
#       return find_right_occurence(arr, start, mid-1, key)
#     else:
#       return find_right_occurence(arr, mid+1, end, key)
  
#   return -1

  # # base condition (out of bounce)
  # if start>end:
  #   return False 

  # if arr[mid] == key:
  #   res = mid 
  #   find_left_occurence(arr, start, mid-1, key)
  # # recursive relation 
  # if arr[mid] < key:
  #   # go to right wala part
  #   res = find_left_occurence(arr, mid+1, end, key)
  #   return res 
  # else:
  #   # go to left wala part  
  #   res = find_left_occurence(arr, start, mid-1, key)
  #   return res 

  # print(res)
  # return -1

# if __name__ == '__main__':
#   arr = [0, 2, 2, 2, 3, 3, 3, 5, 5, 5]
#   n = len(arr)-1
#   out1 = find_left_occurence(arr, 0, n-1, 2)
#   out2 = find_right_occurence(arr, 0, n-1, 2)

#   print("Left most occurence of element is at {} position.".format(out1))
#   print("Right most occurence of element is at {} position.".format(out2))
def find_first_occurence(arr, n, x):
    low, high = 0, len(arr)-1
    
    first = -1
    
    while low <= high:
        mid = (low+high)//2
        
        if arr[mid] == x:
            first = mid
            high = mid-1
        elif x > arr[mid]:
            low = mid + 1
        else:
            high = mid-1
            
    return first 


def find_last_occurence(arr, n, x):
    low, high = 0, len(arr)-1
    last = -1
    
    while low<=high:
        mid = (low+high)//2
        
        if arr[mid] == x:
            last = mid
            low = mid+1
        elif x > arr[mid]:
            low = mid+1
        else:
            high = mid-1
            
    return last 

def find(arr, n, x):
    
    first = find_first_occurence(arr, n, x)
    last = find_last_occurence(arr, n, x)
    
    return first, last

print(find([1, 3, 5, 5, 5, 5, 67, 123], 8, 5))
