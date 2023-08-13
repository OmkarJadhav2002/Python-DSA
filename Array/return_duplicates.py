def find_duplicates(arr):
  res = []
  duplicate_found = False 
    
  for i in arr:
    num = i
    count = 0
    for j in arr:
      if j == num:
        count += 1
    
    if count >= 2:
      if i not in res:
        res.append(i) 
        duplicate_found = True 
    
  if duplicate_found:
    return res 
  else:
    return -1

  # res = set()
  # res = []
  # duplicate_found = False 

  # for i in range(len(arr)):
  #   num = arr[i]
  #   count = 0
  #   for j in range(len(arr)):
  #     if arr[j] == num:
  #       count += 1

  #   if count >= 2:
  #     if arr[i] not in res:
  #       res.append(arr[i]) 
  #       duplicate_found = True 

  # if duplicate_found:
  #   return res 
  # else:
  #   return -1
  
print(find_duplicates([4, 2, 3, 1, 2, 3, 4, 5, 4]))