# 1st Approach:  Sort the array arr.sort()

# 2nd Approach: Partition of Quick sort
# def move_elements(arr):
#   j = 0
#   for i in range(len(arr)):
#     if arr[i] < 0:
#       temp = arr[i]
#       arr[i] = arr[j]
#       arr[j] = temp

#       j += 1

#   return arr

# 3rd Approach: Two pointer
# def move_elements(arr):
#   left, right = 0, len(arr)-1
#   while left <= right:
#     if arr[left] < 0 and arr[right] < 0:
#       left += 1

#     elif arr[left] > 0 and arr[right] < 0:
#       arr[left], arr[right] = arr[right], arr[left]
#       left += 1
#       right -= 1

#     elif arr[left] > 0 and arr[j] > 0:
#       right -= 1

#     else:
#       left += 1
#       right -= 1

#   return arr

# Approach 4: Dutch national flag algorithm
# def move_elements(arr):
#   low, high = 0, len(arr)-1
#   while low < high:
#     if arr[low] < 0:
#       low += 1
#     elif arr[high] > 0:
#       high -= 1
#     else:
#       arr[low], arr[high] = arr[high], arr[low]

#   return arr

# print("New array: ", move_elements([-12, 11, -13, -5, 6, -7, 5, -3, -6]))