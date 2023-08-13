
# Find the first and last occurence of an element 


# Brute Force O(n), O(1)
# def find_first_last(arr, x):
#   first, last = -1, -1

#   for i in range(0, len(arr)-1):
#     if arr[i] == x:
#       if first == -1:
#         first = i 

#       last = i 

#   return [first, last]


# print(find_first_last([2, 8, 8, 12, 8, 23], 8))

# Optimal (Using Binary Search)
def find_first_occurence(arr, x):
  low, high = 0, len(arr)-1
  first = -1
  mid = (low+high)//2
  while low <= high:
    mid = (low+high)//2

    if arr[mid] == x:
      first = mid 
      high = mid-1
    elif x > arr[mid]:
      low = mid+1 # go to right portion
    else:
      high = mid-1 # go to left portion 

  return first 

# print(find_first_occurence([2, 8, 8, 8, 12, 2], 8))

def find_last_occurence(arr, x):
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

print("First occurence: ", find_first_occurence([2, 4, 8, 8, 12, 8, 11, 90], 8))
print("Last occurence: ", find_last_occurence([2, 4, 8, 8, 12, 8, 11, 90], 8))


    