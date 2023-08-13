def reverse_string(st):
  rev = ""
  for i in st:
    rev = i + rev

  return rev
  # l = 0
  # r = len(st)-1

  # while l < r:
  #   st[l], st[r] = st[r], st[l]
  #   l += 1
  #   r -= 1

  # return st

print("Reversed String: ", reverse_string("Omkar"))