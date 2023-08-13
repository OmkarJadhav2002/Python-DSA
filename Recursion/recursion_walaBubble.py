def bubble(arr, n):
  # base case (length of array is 0 or array contains only one element then the array is already sorted)
  if n == 0 or n == 1:
    return 

  # solve for one case 
  for i in range(0, n-1):
    if arr[i] > arr[i+1]:
      arr[i], arr[i+1] = arr[i+1], arr[i]
 
  # recursive relation (sort the remaining window only, after ith largest element reach to the end i.e it's right position, 
  # therefor reducing the length of the array by one)
  bubble(arr, n-1)

if __name__ == '__main__':
  arr = [10, 23, 21, 2, 0, 1]
  n = len(arr)
  bubble(arr, n)
  # print the array    
  for i in range(len(arr)):
    print(arr[i], end=" ")