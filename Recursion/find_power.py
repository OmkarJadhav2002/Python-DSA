def power(a, b):
  
  # base case 
  if b == 0:
    return 1
  if b == 1:
    return a

  ans = power(a, b//2)

  if b%2 == 0:
    return ans*ans 

  else:
    return a*ans*ans 

if __name__ == '__main__':
  res = power(5, 3)
  print(res)