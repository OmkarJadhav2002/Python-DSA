# implementing merge sort using recursion

# merge two sorted arrays 
def merge(arr, s, e):
  
  mid = (s+e)//2

  # length of first array (left array)
  len1 = mid - s + 1
  # length of second array (right array)
  len2 = e - mid

  # creating new arrays for copying the values 
  arr1 = [0]*len1 
  arr2 = [0]*len2

  # copy the values
  arr1Index = s
  for i in range(len1):
    arr1[i] = arr[arr1Index]
    arr1Index += 1

  arr2Index = mid+1
  for i in range(len2):
    arr2[i] = arr[arr2Index]
    arr2Index += 1

  # merge two sorted arrays
  mainArrayIndex = s
  index1, index2 = 0, 0

  while index1<len1 and index2<len2:
    if arr1[index1] < arr2[index2]:
      arr[mainArrayIndex] = arr1[index1]
      mainArrayIndex += 1
      index1 += 1
    else:
      arr[mainArrayIndex] = arr2[index2]
      mainArrayIndex += 1
      index2 += 1

  # copy remaining elements 
  # left array values
  while index1 < len1:
    arr[mainArrayIndex] = arr1[index1]
    mainArrayIndex += 1
    index1 += 1

  # right array values  
  while index2 < len2:
    arr[mainArrayIndex] = arr2[index2]
    mainArrayIndex += 1
    index2 += 1 
    
def mergeSort(arr, s, e):

  # base case 
  if s>=e:
    return 

  mid = (s+e)//2

  # sort left part 
  mergeSort(arr, s, mid);

  # sort right part 
  mergeSort(arr, mid+1, e)

  # merge sorted arrays 
  merge(arr, s, e)


if __name__ == '__main__':
  arr = [12, 1, 23, 31, 2, 2, 0, 89, 8, 56, 10]
  n = len(arr)
  mergeSort(arr, 0, n-1)

  # print sorted array 
  print("Sorted Array: ")
  for i in range(len(arr)):
    print(arr[i], end=" ")