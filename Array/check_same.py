
def check_array(arr1, arr2):

  # if len(arr1) != len(arr2):
  #   return False 

  arr = []
  for i in arr1:
    if i not in arr:
      arr.append(i)

  for j in arr2:
    if j not in arr:
      return False 
    else:
      return True 
  # return arr 

print(check_array([1, 0, 2, 34, 12], [12, 0]))