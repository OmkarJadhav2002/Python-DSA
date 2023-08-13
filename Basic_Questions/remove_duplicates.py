def remove_duplicates_from_sorted(arr):

  # res = set()

  # for i in arr:
  #   if i not in res:
  #     res.add(i)

  # return len(res), list(res) 

  res = set()

  for i in arr:
    res.add(i)

  index = 0
  for i in res:
    arr[index] = i
    index += 1

  return index, arr

print(remove_duplicates_from_sorted([0, 0, 0, 1, 1, 2, 2, 3, 3, 4]))