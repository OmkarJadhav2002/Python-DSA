
def minimizeHeight(arr, n, k):
  # sort the array
  arr.sort()

  # find the max difference first 
  maxDiff = arr[n-1] - arr[0]
  # adding k in smallest ele and subtracting k from largest ele
  smallest = arr[0] + k
  largest = arr[n-1] - k
  # to store the min ele and max ele after updation by k
  maxi = 0
  mini = 0

  for i in range(n-2):
    mini = min(smallest, arr[i]+k)
    maxi = max(largest, arr[n-1]-k)

    if mini < 0:
      continue

    res = min(maxDiff, maxi-mini)

  return res

print("Minimum Difference: ", minimizeHeight([3, 9, 12, 16, 20], 5, 3))
