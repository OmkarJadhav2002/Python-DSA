def valueEqualtoIndex(arr):
  res = []

  for i in range(len(arr)):
    if arr[i] == i+1:
      res.append(arr[i])

  return res 

# print(valueEqualtoIndex([15, 2, 45, 12, 7]))

# print(max([1, 2, 3, 4, 45, 1]))
