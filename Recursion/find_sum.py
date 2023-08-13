def find_sum(arr, n):

  # iterative solution 
  # sum = 0
  # for i in range(n):
  #   sum += arr[i]

  # return sum 


  # recursive solution
  # base case
  sum = 0 
  if n == 0:
    return 0 
  if n == 1:
    return arr[0]

  # recursive relation 
  else:
    # return find_sum(arr, n-1) + arr[n-1]
    remainingPortion = find_sum(arr[1:], n-1)
    sum = arr[0] + remainingPortion

    return sum

if __name__ == '__main__':
  arr = [1, 3, 4]
  n = len(arr)
  ans = find_sum(arr, n)
  print("Sum of array: ", ans)
  