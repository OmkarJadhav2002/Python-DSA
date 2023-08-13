def find_second_largest(arr):
  # two passes
  largest = arr[0]
  slargest = -1
  for i in range(len(arr)):
      if arr[i] > largest:

        largest = arr[i]

  for i in range(len(arr)):
      if arr[i] > slargest and arr[i] != largest:
          slargest = arr[i]

  return slargest

# print(find_second_largest([1, 2, 3, 4, 5, 6]))

def find_second_smallest(arr):
  smallest = arr[0]
  ssmallest = float("inf")

  for i in range(len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]

  for i in range(len(arr)):
    if arr[i] < ssmallest and arr[i]!=smallest:
      ssmallest = arr[i]

  return ssmallest

print(find_second_smallest[2, 3, 4, 5])