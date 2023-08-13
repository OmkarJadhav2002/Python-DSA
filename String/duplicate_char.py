
def find_duplicates(st):
  res = ""
  for i in range(len(st)):
    for j in range(i+1, len(st)):
      if st[i] == st[j]:
        res += st[i]

  # return res
  res.split()

# print(find_duplicates("abacdb"))

import numpy as np
# arr1 = np.array([12, 2, 3, 4])
# arr1 = {(arr1)}
# print(arr1)

# class one:
#   def __init__(self):
#     self.add(5)
#     print(self.i)

#   def add(self, i):
#     self.i = 4 + i

# class Two(one):
#   def __init__(self):
#     super().__init__()
#   def add(self, i):
#     self.i = 2 + i

# work = Two()

# tuple1 = (15, 2, 46, 5)
# t2 = tuple1[-2:0]
# tuple1.pop(2)
# print(tuple1)
# print(t2)
# for tuple in tuple1:
#   print(tuple)


l = ["ab", "cd", "ef", "gh", "ij", "kl"]
m = 2

for i in range(0, 6, m):
  print("".join(l[i:i+m]), end=" ")