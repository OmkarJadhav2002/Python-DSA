
# arr = [1, 2, 3, 4, 5, 6]

# i = 0
# temp = []
# k = 3
# while i < k:
#   temp.append(arr[i])
#   i += 1

# print(temp)

def union(arr1, arr2):
  res = set()

  for i in arr1:
    res.add(i)

  for j in arr2:
    res.add(j)

  return list(res) 

print(union([1, 2, 3, 4, 6], [2, 3, 5]))