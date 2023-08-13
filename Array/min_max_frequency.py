def find_min_max(arr):

  dic = {}

  for i in range(len(arr)):
    if arr[i] in dic:
      dic[arr[i]] += 1
    else:
      dic[arr[i]] = 1

  min_value = min(dic.values())
  max_value = max(dic.values())

  min_value_key = [k for k, v in dic.items() if v == min_value]
  max_value_key = [k for k, v in dic.items() if v == max_value] 

  if min_value == max_value and max_value == min_value:
    return min(min_value_key), min(min_value_key)
  else:
    return max(max_value_key), min(min_value_key)

print(find_min_max([9, 14, 2, 13, 16, 9, 3, 12, 7, 6, 15]))