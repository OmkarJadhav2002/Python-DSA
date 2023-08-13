def doUnion(arr1,n,arr2,m):
  ans = []
  for i in range(n):
    if arr1[i] not in ans:
      ans.append(arr1[i])  

  for j in range(m):
    if arr2[j] not in ans:
      ans.append(arr2[j])

  return len(ans)

print("Number of elements: ", doUnion([1, 2, 3], 3, [1, 2, 3, 4, 5], 5))  