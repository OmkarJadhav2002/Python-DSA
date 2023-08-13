def sorted_arr(arr, n):
  # base case 
  if n == 0 or n == 1:
    return True

  if arr[0] > arr[1]:
    return False 

  # recursive relation 
  else:
    remainingPortion = sorted_arr(arr[1:], n-1)

    return remainingPortion 


if __name__ == '__main__':
  array = [11, 2, 9, 9, 9]
  n = len(array)
  ans = sorted_arr(array, n)

  if ans:
    print("Array is sorted.")
  else:
    print("Array is not sorted.")
  