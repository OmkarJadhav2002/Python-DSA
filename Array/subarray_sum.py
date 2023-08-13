
# find total number of subarrays whose sum equals to k 

def subarraySum(arr, k):

  count = 0

  for i in range(len(arr)):
    sum = 0
    for j in range(i, len(arr)):
      sum += arr[j]

      if sum == k:
        count += 1

  return count 

print(subarraySum([1, 2, 3], 3))