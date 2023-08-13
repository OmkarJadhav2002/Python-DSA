def find_missing(arr):

  expected_total = 0
  i = 0
  while i <= len(arr)+1:
    expected_total += i
    i += 1

  return expected_total 

# print(find_missing([0, 1, 3]))