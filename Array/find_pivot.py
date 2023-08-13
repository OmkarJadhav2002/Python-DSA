def find_pivot(arr):
  s, e = 0, len(arr)-1
  mid = (s+e)//2

  while s < e:
    if arr[mid] >= arr[0]:
      s = mid + 1
    else:
      e = mid  # ** not mid-1(see notebook)

    mid = (s+e)//2

  return s

print("Pivot element is at index: ", find_pivot([7, 9, 10, 1, 1, 2, 3]))