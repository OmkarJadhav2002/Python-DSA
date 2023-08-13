
# def find_occurence(arr):

#   dic = {}

#   for i in range(len(arr)):
#     if arr[i] in dic:
#       dic[arr[i]] += 1

#     else:
#       dic[arr[i]] = 1

    
#   for v in dic.values():
#     return v 
  # dic = {}

  # for i in range(len(arr)):
  #   if arr[i] in dic:
  #     dic[arr[i]] += 1
  #   else:
  #     dic[arr[i]] = 1

  # return dic

# print(find_occurence([1, 2, 0, 2, 3, 1, 9, 0, 2]))
arr = [1, 2, 0, 2, 3, 1, 9, 0, 2]

dic = {}

for i in range(len(arr)):
  if arr[i] in dic:
    dic[arr[i]] += 1
  else:
    dic[arr[i]] = 1

for key, value in dic.items():
  print(key, end=": ")
  print(value)