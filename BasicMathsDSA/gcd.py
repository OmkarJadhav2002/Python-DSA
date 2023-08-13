def find_gcd(a, b):
  if a == 0:
    return b
  if b == 0:
    return a

  while a != b:
    if a > b:
      a = a - b
    else:
      b = b - a

  return a

print(find_gcd(74, 24))