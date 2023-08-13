def climbing_Stairs(num):
  # base case  (stairs can't be negative)
  if num < 0:
    return 0

  if num == 0:
    return 1

  ans = climbing_Stairs(num-1) + climbing_Stairs(num-2)

  return ans

if __name__ == '__main__':
  num = int(input("Enter a number: "))
  res = climbing_Stairs(num)
  print(res)